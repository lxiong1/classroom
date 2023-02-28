from django.urls import path
from .views import dashboard

app_name = "demo"

urlpatterns = [
    path("", dashboard, name="dashboard"),
]
