from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    biography = models.TextField(blank=True)

    def __str__(self):
        return f\"{self.user.username}'s Profile\"
