from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_coach = models.BooleanField(default=False)
    country = models.CharField(max_length=5, default='USA')
