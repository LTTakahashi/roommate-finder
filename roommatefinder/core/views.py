# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')  # or wherever you want to redirect
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
            return redirect('update_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'update_profile.html', {'form': form})


def search_profiles(request):
    query_location = request.GET.get('location', '')
    profiles = Profile.objects.all()
    if query_location:
        profiles = profiles.filter(location__icontains=query_location)
    return render(request, 'search.html', {'profiles': profiles})
