from django.contrib import admin
from .models import OldPaper, Project, Blog , SiteSettings

admin.site.register(OldPaper)
admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(SiteSettings)
