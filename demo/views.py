from django.shortcuts import render

def homepage(request):
    return render(request, "pages/home-page.html")

def signup(request):
    return render(request, "pages/signup-page.html")
