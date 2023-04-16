from django.contrib import admin
from core import models
from core import admin_models

# Register your models here.
admin.site.register(models.ShortenedURL, admin_models.ShortenedURIAdmin)
admin.site.register(models.RedirectLog, admin_models.RedirectLogAdmin)
