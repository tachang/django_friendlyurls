from django.contrib import admin
from friendlyurls.models import *

class UrlMappingAdmin(admin.ModelAdmin):
  pass
admin.site.register(UrlMapping, UrlMappingAdmin)

