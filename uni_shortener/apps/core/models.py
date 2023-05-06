from django.db import models
from uni_shortener.apps.core import utils
from datetime import datetime


class ShortenedURL(models.Model):
    url = models.CharField(max_length=255, unique=True)
    hash = models.CharField(max_length=6, unique=True, default=utils.generate_url_hash)
    date_created = models.DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return self.hash


class RedirectLog(models.Model):
    date_redirected = models.DateTimeField(default=datetime.utcnow)

    shortened_link = models.ForeignKey(ShortenedURL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date_redirected)
