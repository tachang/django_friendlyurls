from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
  (r'^.*/', 'friendlyurls.views.resolve_friendly_url'),
)
