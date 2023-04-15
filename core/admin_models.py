from django.contrib import admin


class URIAdmin(admin.ModelAdmin):
    list_display = ("hash", "url", "date_created")
    date_created = ("launch_date",)
    search_fields = ("url", "hash")

    readonly_fields = ["date_created"]
