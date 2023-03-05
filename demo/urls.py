from django.urls import path
from .views import home_page, signup_user, login_user, logout_user

app_name = "demo"

urlpatterns = [
    path("", home_page, name="home-page"),
    path("accounts/signup/", signup_user, name="signup-page"),
    path("accounts/login/", login_user, name="login-page"),
    path("accounts/logout/", logout_user, name="logout-page"),
]
