from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class TextPost(models.Model):
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.content



class HouseUserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    avatar_url = models.URLField(null=True, blank=True)




@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        HouseUserProfile.objects.create(user=instance)
    instance.houseuserprofile.save()
    