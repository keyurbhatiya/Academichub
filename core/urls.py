from django.urls import path,include
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .views import CustomPasswordChangeView, profile_view  # Assuming profile is your profile view
from django.contrib.auth.views import PasswordChangeDoneView
from academichub.auth_urls import urlpatterns as auth_urls

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/paper/', views.upload_paper, name='upload_paper'),
    path('upload/project/', views.upload_project, name='upload_project'),
    path('papers/', views.papers, name='papers'),
    path('projects/', views.projects, name='projects'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/create/', views.blog_create, name='blog_create'),
    path('auth/', include('academichub.auth_urls')),
   
    path('uploads/', views.user_uploads_view, name='user_uploads'),

    # path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
