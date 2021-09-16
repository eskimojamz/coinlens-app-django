from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class UserProf(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    followed_coins = models.JSONField(blank=True, default=dict)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username