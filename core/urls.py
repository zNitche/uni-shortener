from django.urls import path
from core import views


app_name = "core"

urlpatterns = [
    path("", views.main, name="main"),
    path("l/<str:target_hash>", views.redirect_to_target, name="redirect_to_target"),
    path("preview/<str:hash>", views.shortened_url_preview, name="shortened_url_preview")
]
