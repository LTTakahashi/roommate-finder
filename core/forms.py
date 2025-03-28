from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class ProfileUpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=False)  # New field for Name
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], required=False)  # New field for Gender
    budget = forms.DecimalField(max_digits=10, decimal_places=2, required=False)  # New field for Budget
    pet = forms.ChoiceField(choices=[
        ('Pet Preference', 'Pet Preference'),
        ('No Pets', 'No Pets'),
        ('I have a pet/ no preference', 'I have a pet/ no preference')
    ], required=False)  # Updated choices for Pet
    smoke = forms.ChoiceField(choices=[
        ('Smoke Preference', 'Smoke Preference'),
        ('I smoke/ no preference', 'I smoke/ no preference'),
        ('No Smoking', 'No Smoking')
    ], required=False)  # Updated choices for Smoke
    loudness = forms.ChoiceField(choices=[
        ('Volume Preference', 'Volume Preference'),
        ('Quiet', 'Quiet'),
        ('Moderate with occasional loudness', 'Moderate with occasional loudness'),
        ('No preference', 'No preference')
    ], required=False)  # Updated choices for Loudness
    cleanliness = forms.ChoiceField(choices=[
        ('Hygiene/Area Preference', 'Hygiene/Area Preference'),
        ('No preference', 'No preference'),
        ('I prefer a standard clean hygiene/area', 'I prefer a standard clean hygiene/area'),
        ('I prefer an above standard clean hygiene/area', 'I prefer an above standard clean hygiene/area')
    ], required=False)  # Updated choices for Cleanliness
    gender_preference = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Any', 'Any')], required=False)  # New field for Gender Preference

    class Meta:
        model = Profile
        fields = ['name', 'age', 'gender', 'location', 'bio', 'budget', 'pet', 'smoke', 'loudness', 'cleanliness', 'gender_preference']  # Updated fields list
