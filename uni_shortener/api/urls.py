from django.urls import path
from api import views


app_name = "api"

urlpatterns = [
    path("redirects_per_day/<str:month_date>/", views.redirects_per_day, name="redirects_per_day"),
    path("redirects_per_hour/<str:day_date>/", views.redirects_per_hour, name="redirects_per_hour"),
]
