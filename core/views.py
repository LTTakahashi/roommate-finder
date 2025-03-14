from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm

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
    return render(request, 'profile.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
