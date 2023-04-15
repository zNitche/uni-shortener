from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseServerError
from django.views.decorators.http import require_http_methods
from core import models
from core import forms


@require_http_methods(["GET", "POST"])
def main(request):
    form = forms.ShortenedURLCreationForm(data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("core:main")

        else:
            existing_shortened_url = get_object_or_404(models.ShortenedURL, url=form.data.get("url"))
            return redirect("core:shortened_url_preview", hash=existing_shortened_url.hash)

    return render(request, "main.html", {"form": form})


@require_http_methods(["GET"])
def shortened_url_preview(request, hash):
    shortened_url = models.ShortenedURL.objects.filter(hash=hash).first()

    if shortened_url is None:
        return HttpResponseServerError()

    context = {
        "target_url": shortened_url.url,
        "date_created": shortened_url.date_created
    }

    return render(request, "preview.html", context)


@require_http_methods(["GET"])
def redirect_to_target(request, target_hash):
    shortened_url = get_object_or_404(models.ShortenedURL, hash=target_hash)

    return redirect(shortened_url.url)
