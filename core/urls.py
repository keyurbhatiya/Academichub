from django.urls import path
from . import views

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
    # path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),

]