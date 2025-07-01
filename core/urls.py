from django.urls import path,include
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

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
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('blog/<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('blog/<slug:slug>/reply/', views.add_reply, name='add_reply'),
    path('comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),
    path('reply/<int:reply_id>/like/', views.like_reply, name='like_reply'),
    path('user/', include('academichub.auth_urls')),
    path('help-center/', views.help_center, name='help_center'),
    path('contact/', views.contact_us, name='contact'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('community-guidelines/', views.community_guidelines, name='community_guidelines'),
    path('faq/', views.faq_page, name='faqs'),



   
    path('uploads/', views.user_uploads_view, name='user_uploads'),

    # path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
