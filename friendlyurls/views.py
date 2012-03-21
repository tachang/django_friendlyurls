import logging
from friendlyurls.models import *
from django.core.urlresolvers import resolve
from django.http import HttpResponseForbidden, HttpResponse, Http404

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

    redirection = UrlMapping.objects.get(friendly_path = start_path)
    log.debug("URL mapping found. Returning view for: %s" % redirection.absolute_path)

    request.previous_url = redirection.absolute_path

    if( remaining_path != '' ):
      view, args, kwargs = resolve("%s/%s" % (redirection.absolute_path, remaining_path))
    else:
      view, args, kwargs = resolve(redirection.absolute_path)

    kwargs['request'] = request
    return view(*args, **kwargs)

  except UrlMapping.DoesNotExist:
    log.error("No URL mapping exists for: %s" % request.path)
    raise Http404

