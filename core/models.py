# core/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)  # New field for Name
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True)  # New field for Gender
    location = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # New field for Budget
    pet = models.BooleanField(default=False)  # New field for Pet
    smoke = models.BooleanField(default=False)  # New field for Smoke
    loudness = models.CharField(max_length=10, choices=[('Quiet', 'Quiet'), ('Moderate', 'Moderate'), ('Loud', 'Loud')], blank=True)  # New field for Loudness
    cleanliness = models.CharField(max_length=10, choices=[('Messy', 'Messy'), ('Average', 'Average'), ('Clean', 'Clean')], blank=True)  # New field for Cleanliness
    gender_preference = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Any', 'Any')], blank=True)  # New field for Gender Preference

    def __str__(self):
        return f"{self.user.username}'s Profile"
