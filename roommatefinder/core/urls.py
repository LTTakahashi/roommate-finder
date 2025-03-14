from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    # Profile
    path('profile/', views.update_profile, name='update_profile'),
    
    # Search
    path('search/', views.search_profiles, name='search_profiles'),
    
    # Chat
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
]
