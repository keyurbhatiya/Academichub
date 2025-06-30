from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views


urlpatterns = [
    path('admin/',views.admin_dashboard, name='admin_dashboard'),
    path('admin/users/', views.admin_users, name='admin_users'),
    path('admin/papers/', views.admin_papers, name='admin_papers'),
    path('admin/projects/', views.admin_projects, name='admin_projects'),
    path('admin/blogs/', views.admin_blogs, name='admin_blogs'),
    path('admin/content-moderation/', views.Content_Moderation, name='content_moderation'),
    path('admin/users/<int:user_id>/profile/', views.view_user_profile, name='view_user_profile'),
    path('admin/users/<int:user_id>/deactivate/', views.deactivate_user, name='deactivate_user'),
    path('admin/users/<int:user_id>/activate/', views.activate_user, name='activate_user'),
    path('admin/papers/upload/', views.upload_old_paper, name='upload_old_paper'),
    path('admin/analytics/', views.analytics, name='analytics'),
    path('admin/settings/', views.settings, name='settings'),

    # path('admin/', admin.site.urls),
    path('', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)