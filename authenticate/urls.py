from django.urls import path
from authenticate import views


app_name = "authenticate"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("2fa/<str:token>", views.second_fa_auth, name="second_fa_auth"),
]
