from django.contrib import admin
from core.models import ShortenedURL
from core.admin_models import URIAdmin

# Register your models here.
admin.site.register(ShortenedURL, URIAdmin)
