from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followed_coins = models.JSONField(encoder=None, decoder=None)

# class Transaction(models.Model):
#     coin = models.CharField(
#         max_length=50, 
#         null=True
#     )
#     TYPE_CHOICES = [
#         ('BUY', 'Buy'),
#         ('SELL', 'Sell')
#     ]
#     type = models.CharField(
#         max_length=4,
#         choices=TYPE_CHOICES,
#         null=True
#     )
#     amount_ = models.DecimalField(
#         max_digits=50,
#         decimal_places=8,
#         null=True
#     )
#     transaction_date = models.DateTimeField(null=True)
#     userId = models.CharField(max_length=20, null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)