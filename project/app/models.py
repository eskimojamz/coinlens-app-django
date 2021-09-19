from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProf(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    followed_coins = models.TextField(max_length=None)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProf.objects.create(user=instance)
    instance.userprof.save()