from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate as auth_user
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.cache import cache
from uni_shortener.apps.authenticate import forms
from django.contrib.auth import get_user_model
import pyotp


@require_http_methods(["GET", "POST"])
def login(request):
    if not request.user.is_authenticated:
        form = forms.LoginForm(data=request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                username = request.POST["username"]
                password = request.POST["password"]

                user = auth_user(request, username=username, password=password)

                if user is not None:
                    if user.second_fa_token:
                        cache.set(f"user-2fa-request-{request.session.session_key}", user.id, 90)

                        return redirect("authenticate:second_fa_auth")

                    else:
                        auth_login(request, user)
                        messages.add_message(request, messages.SUCCESS, "logged in")

                        return redirect(settings.LOGIN_REDIRECT_URL)

                messages.add_message(request, messages.ERROR, "error while logging in")

        return render(request, "login.html", {"form": form})

    else:
        return redirect(settings.LOGIN_REDIRECT_URL)


@require_http_methods(["GET", "POST"])
def second_fa_auth(request):
    auth_request_cache_key = f"user-2fa-request-{request.session.session_key}"
    user_id = cache.get(auth_request_cache_key)

    if not request.user.is_authenticated and user_id:
        form = forms.SecondFAForm(data=request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                auth_code = request.POST["auth_code"]
                user = get_user_model().objects.filter(pk=user_id).first()

                if user:
                    totp = pyotp.TOTP(user.second_fa_token)

                    if totp.verify(auth_code):
                        auth_login(request, user)
                        cache.delete(auth_request_cache_key)
                        messages.add_message(request, messages.SUCCESS, "logged in")

                        return redirect(settings.LOGIN_REDIRECT_URL)

                    else:
                        messages.add_message(request, messages.ERROR, "wrong auth code")

        return render(request, "2fa_auth.html", {"form": form})

    return redirect(settings.LOGIN_REDIRECT_URL)


@login_required
@require_http_methods(["GET"])
def logout(request):
    auth_logout(request)

    return redirect(settings.LOGIN_REDIRECT_URL)
