# core/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)

    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg', blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
