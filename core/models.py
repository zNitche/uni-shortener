from django.db import models
from core import utils
from datetime import datetime


class ShortenedURL(models.Model):
    url = models.CharField(max_length=255, unique=True)
    hash = models.CharField(max_length=6, unique=True, default=utils.generate_url_hash)
    date_created = models.DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return self.hash
