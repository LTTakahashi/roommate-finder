from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm, ProfileUpdateForm, ProfileFilterForm
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
    # Initialize the advanced filter form with GET data
    form = ProfileFilterForm(request.GET or None)
    results = Profile.objects.none()  # default empty queryset

    if form.is_valid():
        # Retrieve filter criteria from the form
        username = form.cleaned_data.get('username')
        location = form.cleaned_data.get('location')
        min_age = form.cleaned_data.get('min_age')
        max_age = form.cleaned_data.get('max_age')
        bio_keyword = form.cleaned_data.get('bio_keyword')

        # Build the query dynamically
        query = Q()
        if username:
            query &= Q(user__username__icontains=username)
        if location:
            query &= Q(location__icontains=location)
        if min_age is not None:
            query &= Q(age__gte=min_age)
        if max_age is not None:
            query &= Q(age__lte=max_age)
        if bio_keyword:
            query &= Q(bio__icontains=bio_keyword)

        results = Profile.objects.filter(query)

    context = {
        'form': form,
        'profiles': results,
    }
    return render(request, 'search.html', context)

@login_required
def chat_room(request, username):
    current_user = request.user
    other_user = get_object_or_404(User, username=username)

    room_name = f'{current_user.username}-{other_user.username}'
    ordered_room_name = '-'.join(sorted([current_user.username, other_user.username]))

    return render(request, 'chat_room.html', {
        'room_name': ordered_room_name,  # Pass EXACTLY this
        'other_user': other_user,
    })