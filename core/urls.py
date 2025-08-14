from django.urls import path, include, re_path
from django.views.static import serve
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeDoneView
from academichub.auth_urls import urlpatterns as auth_urls
import os

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('papers/', views.papers, name='papers'),
    path('projects/', views.projects, name='projects'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
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
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('cookie-policy/', views.cookie_policy, name='cookie_policy'),
    path('uploads/', views.user_uploads_view, name='user_uploads'),
    path('ads.txt', views.ads_txt_view, name='ads_txt'),
]

# ✅ Custom error handlers (must be at module level)
handler404 = 'core.views.custom_404'
handler500 = 'core.views.custom_500'
