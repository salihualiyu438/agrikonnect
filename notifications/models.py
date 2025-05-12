from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s request"
    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/')

    def __str__(self):
        return f"{self.user.username}'s profile"