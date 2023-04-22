from django.shortcuts import render, redirect, resolve_url
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate as auth_user
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.cache import cache
from authenticate import forms
import secrets
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
                        auth_token = secrets.token_urlsafe(64)
                        cache.set(f"auth-user-{auth_token}", user, 120)

                        return redirect("authenticate:second_fa_auth", token=auth_token)

                    else:
                        auth_login(request, user)
                        messages.add_message(request, messages.SUCCESS, "logged in")

                        return redirect(settings.LOGIN_REDIRECT_URL)

                messages.add_message(request, messages.ERROR, "error while logging in")

        return render(request, "login.html", {"form": form})

    else:
        return redirect(settings.LOGIN_REDIRECT_URL)


@require_http_methods(["GET", "POST"])
def second_fa_auth(request, token):
    user = cache.get(f"auth-user-{token}")

    if not request.user.is_authenticated and user:
        form = forms.SecondFAForm(data=request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                auth_code = request.POST["auth_code"]

                if user:
                    totp = pyotp.TOTP(user.second_fa_token)

                    if totp.verify(auth_code):
                        auth_login(request, user)
                        cache.delete(f"auth-user-{token}")
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
