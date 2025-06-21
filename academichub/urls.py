from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views


urlpatterns = [
    path('admin/',views.admin_dashboard, name='admin_dashboard'),
    path('admin/user/', views.admin_users, name='admin_users'),
    path('admin/papers/', views.admin_papers, name='admin_papers'),
    path('admin/projects/', views.admin_projects, name='admin_projects'),
    path('admin/blogs/', views.admin_blogs, name='admin_blogs'),
    path('admin/content-moderation/', views.Content_Moderation, name='content_moderation'),
    # path('admin/', admin.site.urls),
    path('', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)