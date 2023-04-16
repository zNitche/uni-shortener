from django.contrib import admin


class ShortenedURIAdmin(admin.ModelAdmin):
    list_display = ("hash", "url", "date_created")
    search_fields = ("url", "hash")

    readonly_fields = ["date_created", "hash"]


class RedirectLogAdmin(admin.ModelAdmin):
    list_display = ("date_redirected", "shortened_link")
    search_fields = ("date_redirected", "shortened_link")

    readonly_fields = ["date_redirected", "shortened_link"]
