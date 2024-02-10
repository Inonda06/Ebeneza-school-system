from django.db import models
from ebenezamanagement.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    ProfilePic=models.ImageField(upload_to="media", blank=True, null=True)

    def __str__(self):
        return f'Profile of {self.user.username}'