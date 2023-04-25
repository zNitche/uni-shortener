from django.urls import path
from management import views


app_name = "management"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
]
