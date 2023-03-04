from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login


def homepage(request):
    return render(request, "pages/home-page.html")


def signup(request):
    if request.method == "POST":
        data = request.POST
        signup_info = User(
            profile_type=data.get("profile_type"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            email=data.get("email"),
            password=data.get("password"),
        )
        user = signup_info.save()
        login(request, user)

        return redirect("demo:home-page")

    return render(request, "pages/signup-page.html")
