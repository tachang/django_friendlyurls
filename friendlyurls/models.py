from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.core.cache import cache
from django.dispatch import receiver

class UrlMapping(models.Model):
  friendly_path = models.CharField(max_length=512, db_index=True, unique=True)
  content_type = models.ForeignKey(ContentType)
  object_id = models.CharField(max_length=256)
  content_object = generic.GenericForeignKey()
  created = models.DateTimeField(auto_now=True, blank=True)

  def __unicode__(self):
    return "%s" % (self.friendly_path)

  def resolved_url(self):
    """Call get_absolute_url() on the content_object and return the url.
    """
    return self.content_object.get_absolute_url()

  def object(self):
    return str(self.content_object)

@receiver(pre_save, sender=UrlMapping)
def urlmapping_pre_save_handler(sender, instance=None, raw=True, **kwargs):
  if instance:
    # Get the old value and invalidate the cache
    for urlmapping in UrlMapping.objects.filter(pk=instance.id):
      cache.delete(urlmapping.friendly_path)
