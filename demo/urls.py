from django.urls import path
from .views import homepage, signup

app_name = "demo"

urlpatterns = [
    path("", homepage, name="home-page"),
    path("accounts/signup/", signup, name="signup-page"),
]
