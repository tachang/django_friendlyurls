from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

class UrlMapping(models.Model):
  friendly_path = models.CharField(max_length=512, db_index=True, unique=True)
  absolute_path = models.CharField(max_length=512, db_index=True)
  content_type = models.ForeignKey(ContentType)
  object_id = models.CharField(max_length=256)
  content_object = generic.GenericForeignKey()

  created = models.DateTimeField(auto_now=True, blank=True)

  def __unicode__(self):
    return "%s" % (self.friendly_path)

User.add_to_class('friendly_urls', generic.GenericRelation(UrlMapping))
