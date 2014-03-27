import logging
from friendlyurls.models import *
from django.core.urlresolvers import resolve
from django.http import HttpResponseForbidden, HttpResponse, Http404
from django.conf import settings
from django.core.cache import cache

log = logging.getLogger(__name__)

def resolve_friendly_url(request):

  # Check to see if the abort attribute exists on request. If it does it means
  # it was set previously from a resolve_friendly_url call.
  if( getattr(request, 'abort', None) != None ):
    log.error("Error returning view for friendlyurl. Please check that %s is a valid url." % request.previous_url)
    raise Http404

  # Check to see if there is a redirect for this URL
  try:
    # Make sure we only try to resolve vanity URLs a single time
    request.abort = True

    start_path, sep, remaining_path = request.path.strip('/').partition('/')
    log.debug("Lookup path [%s] | [%s]" % (start_path, remaining_path) )

    obj_absolute_url = cache.get(start_path)

    # If the url is not in the cache then retrieve it from the database
    if not obj_absolute_url:
    
      if( settings.FRIENDLYURLS_IGNORE_CASE == True ):
        redirection = UrlMapping.objects.get(friendly_path__iexact = start_path)
      else:
        redirection = UrlMapping.objects.get(friendly_path = start_path)

      log.debug("URL mapping found. Returning get_absolute_url() on %s" % redirection.content_object)

      # Absolute URL for object
      obj_absolute_url = redirection.content_object.get_absolute_url()

      cache.set(start_path, obj_absolute_url, 3600)

    request.previous_url = obj_absolute_url

    if( remaining_path != '' ):
      view, args, kwargs = resolve("%s/%s" % (obj_absolute_url, remaining_path))
    else:
      view, args, kwargs = resolve(obj_absolute_url)

    kwargs['request'] = request
    return view(*args, **kwargs)



  except UrlMapping.DoesNotExist:
    log.error("No URL mapping exists for: %s" % request.path)
    raise Http404
