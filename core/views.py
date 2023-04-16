from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.http import HttpResponseServerError
from django.views.decorators.http import require_http_methods
from django.contrib import messages
# from django.urls import reverse
from core import models
from core import forms


@require_http_methods(["GET", "POST"])
def main(request):
    form = forms.ShortenedURLCreationForm(data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            shortened_url = form.save()

            return redirect("core:shortened_url_preview", hash=shortened_url.hash)

        else:
            existing_shortened_url = get_object_or_404(models.ShortenedURL, url=form.data.get("url"))

            return redirect("core:shortened_url_preview", hash=existing_shortened_url.hash)

    return render(request, "main.html", {"form": form})


@require_http_methods(["GET", "POST"])
def search_created_url(request):
    form = forms.ShortenedURLSearchForm(data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            existing_shortened_url = models.ShortenedURL.objects.filter(hash=form.data.get("hash")).first()

            if existing_shortened_url:
                return redirect("core:shortened_url_preview", hash=existing_shortened_url.hash)

            else:
                messages.add_message(request, messages.ERROR, "shortened link doesn't exist")

    return render(request, "search_created_url.html", {"form": form})


@require_http_methods(["GET"])
def shortened_url_preview(request, hash):
    shortened_url = models.ShortenedURL.objects.filter(hash=hash).first()

    if shortened_url is None:
        return HttpResponseServerError()

    # redirect_url = reverse("core:redirect_to_target", kwargs={"target_hash":shortened_url.hash})
    redirect_url = resolve_url("core:redirect_to_target", target_hash=shortened_url.hash)

    context = {
        "shortened_url": shortened_url,
        "redirect_url": request.build_absolute_uri(redirect_url),
    }

    return render(request, "preview.html", context)


@require_http_methods(["GET"])
def redirect_to_target(request, target_hash):
    shortened_url = get_object_or_404(models.ShortenedURL, hash=target_hash)

    redirect_log = models.RedirectLog(shortened_link=shortened_url)
    redirect_log.save()

    return redirect(shortened_url.url)
