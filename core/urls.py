from django.urls import path
from core import views


app_name = "core"

urlpatterns = [
    path("", views.main, name="main"),
    path("search/", views.search_created_url, name="search_created_url"),
    path("go/<str:target_hash>", views.redirect_to_target, name="redirect_to_target"),
    path("l/<str:hash>", views.shortened_url_preview, name="shortened_url_preview")
]
