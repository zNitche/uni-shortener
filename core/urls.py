from django.urls import path
from core import views


app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("<str:target_hash>", views.redirect_to_target, name="redirect_to_target")
]
