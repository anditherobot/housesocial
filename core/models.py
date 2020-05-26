from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# User Models

class HeartBeat(models.Model):
    beat = models.BooleanField()


class CoreUserProfile(models.Model):
    user = models.OneToOneField(User, related_name='coreuserprofile', on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    avatar_url = models.URLField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        CoreUserProfile.objects.create(user=instance)
    instance.coreuserprofile.save()
