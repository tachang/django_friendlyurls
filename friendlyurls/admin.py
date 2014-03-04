from django.contrib import admin
from friendlyurls.models import *

class UrlMappingAdmin(admin.ModelAdmin):
  list_display = ('friendly_path', 'resolved_url', 'content_type', 'object')
  search_fields = ['friendly_path','content_type__name']
admin.site.register(UrlMapping, UrlMappingAdmin)

