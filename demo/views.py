from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout
import logging

logger = logging.getLogger(__name__)

def home_page(request):
    if request.user.is_authenticated:
        return render(request, "pages/home-page.html")


def signup_user(request):
    if request.method == "POST":
        data = request.POST
        signup_info = User(
            profile_type=data.get("profile_type"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            username=data.get("username"),
            email=data.get("email"),
            password=data.get("password"),
        )
        logger.info(vars(signup_info))
        user = signup_info.save()
        login(request, user)

        return redirect("demo:home-page")

    return render(request, "pages/signup-page.html")

def login_user(request):
    logger.info(request)
    if request.method == "POST":
        data = request.POST
        user = authenticate(username=data.get("username"), password=data.get("password"))
        logger.info(user)

        if user:
            login(request, user)

            return redirect("demo:home-page")

    return render(request, "pages/login-page.html")

def logout_user(request):
    if request.method == "POST":
        logout(request)

        return redirect("demo:logout-page.html")
