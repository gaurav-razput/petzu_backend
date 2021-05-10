from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=20)
    REQUIRED_FIELDS = ['password']
    USERNAME_FIELD = 'username'
