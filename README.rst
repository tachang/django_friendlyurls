This Django application allows you to create urls that directly return views.
There is no 302 Redirect.

The most common use case is that you have URLs which return user profiles such as

http://www.example.com/user/1

Friendly URLs allow you to create a URL so that the user can also be accessed by going to:

http://www.example.com/jeff

The key is that the address bar in the browser does not change to http://www.example.com/user/1
The web server returns the same HTML document as http://www.example.com/user/1

Flow
-----

The application looks up the string 'jeff' If it finds a friendly url match it will read out the absolute_path
and attempt to resolve it by putting it through the URL resolver a 2nd time.

If it finds a resolution it will return that view.


Usage
-----

Here is an example of how to implement friendly_urls for a user:

I put this in models.py:

from django.contrib.contenttypes import generic
from friendlyurls import UrlMapping
from django.contrib.auth.models import User

def get_absolute_url(self):
  return u'/user/%s' % self.id

User.add_to_class('friendly_urls', generic.GenericRelation(UrlMapping))
User.get_absolute_url = get_absolute_url

This basically monkey patches the User model to add a field. You can then do

user = User.objects.get(pk=1)
user.friendly_urls.all()

This will get a list of all the friendly urls.

You shouldn't have to monkey patch all the models.

Problems / Questions
--------------------

Don't forget to run syncdb because friendlyurls creates a table to store the URL mappings.


Todo Features
-------------

- Need to cache the results returned by a lookup for performance.
Probably do a from django.core.cache import cache

https://docs.djangoproject.com/en/dev/topics/cache/?from=olddocs
