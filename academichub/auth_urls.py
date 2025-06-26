# yourapp/auth_urls.py
from django.urls import path
from django.contrib.auth.decorators import login_required
from core.views import CustomPasswordChangeView, profile_view

urlpatterns = [
    path('profile/', login_required(profile_view), name='profile'),
    path('password_change/', login_required(CustomPasswordChangeView.as_view()), name='password_change'),
]
