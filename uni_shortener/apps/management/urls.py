from django.urls import path
from uni_shortener.apps.management import views


app_name = "management"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
]
