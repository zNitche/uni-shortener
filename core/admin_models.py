from django.contrib import admin


class URIAdmin(admin.ModelAdmin):
    list_display = ("hash", "org_url", "date_created")
    date_created = ("launch_date",)
    search_fields = ("org_url", "hash")

    readonly_fields = ["date_created"]
