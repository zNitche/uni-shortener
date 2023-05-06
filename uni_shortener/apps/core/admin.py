from django.contrib import admin
from uni_shortener.apps.core import models
from uni_shortener.apps.core import admin_models

# Register your models here.
admin.site.register(models.ShortenedURL, admin_models.ShortenedURIAdmin)
admin.site.register(models.RedirectLog, admin_models.RedirectLogAdmin)
