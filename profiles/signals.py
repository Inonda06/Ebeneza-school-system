from profiles.models import UserProfile
from ebenezamanagement.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=User)
def post_save_create_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)