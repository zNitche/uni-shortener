from django.urls import path
from uni_shortener.apps.authenticate import views


app_name = "authenticate"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("login/2fa/", views.second_fa_auth, name="second_fa_auth"),
]
