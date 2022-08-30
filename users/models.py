from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length=20)
    birth_year = models.CharField(max_length=4)
    birth_month = models.CharField(max_length=2)
    birth_day = models.CharField(max_length=2)
    gender = models.CharField(max_length=10)