from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from core.models import ShortenedURL


@require_http_methods(["GET"])
def home(request):
    return render(request, "home.html")


@require_http_methods(["GET"])
def redirect_to_target(request, target_hash):
    shortened_url = get_object_or_404(ShortenedURL, hash=target_hash)

    return redirect(shortened_url.org_url)
