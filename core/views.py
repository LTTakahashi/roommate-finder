from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm, ProfileUpdateForm
from django.db.models import Q
from .models import Profile


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profile.html', {'form': form})
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def search_profiles(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        results = Profile.objects.filter(
            Q(user__username__icontains=query) |
            Q(location__icontains=query) |
            Q(bio__icontains=query)
        )

    context = {
        'profiles': results,
        'query': query,
    }
    return render(request, 'search.html', context)

@login_required
def chat_room(request, username):
    other_user = get_object_or_404(User, username=username)

    room_name = "-".join(sorted([request.user.username, other_user.username]))

    return render(request, 'chat_room.html', {
        'room_name': room_name,
        'other_user': other_user,
    })