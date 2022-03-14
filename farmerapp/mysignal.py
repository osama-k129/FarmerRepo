from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import User_profile


#connecting profile to user table that is allredy exist
@receiver(post_save, sender=User)
def save_User_profile(sender, instance, created, **kwarg):
    if created:
        User_profile.objects.create(user=instance)



