from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class UserProf(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    followed_coins = models.JSONField(blank=True, default=dict)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email