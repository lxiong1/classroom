from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_type = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
