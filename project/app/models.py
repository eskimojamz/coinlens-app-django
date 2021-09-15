from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProf(AbstractUser):
    followed_coins = models.JSONField(null=True)