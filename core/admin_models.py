from django.contrib import admin


class URIAdmin(admin.ModelAdmin):
    list_display = ("hash", "url", "date_created")
    search_fields = ("url", "hash")

    readonly_fields = ["date_created"]
