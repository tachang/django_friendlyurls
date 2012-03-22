from django.contrib import admin
from friendlyurls.models import *

class UrlMappingAdmin(admin.ModelAdmin):
  list_display = ('friendly_path', 'resolved_url', 'content_type', 'object')
admin.site.register(UrlMapping, UrlMappingAdmin)

