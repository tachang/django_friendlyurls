This Django application allows you to create urls that directly return views.

The most common use case is that you have URLs which return user profiles such as

http://www.example.com/user/1

Friendly URLs allow you to create a URL so that the user can also be access by going to:

http://www.example.com/jeff

Flow
-----

The application looks up the string 'jeff' If it finds a friendly url match it will read out the absolute_path
and attempt to resolve it by putting it through the URL resolver a 2nd time.

If it finds a resolution it will return that view.


Usage
-----

Here is an example of how to implement friendly_urls for a user:

I put this in models.py:

from django.contrib.auth.models import User
User.add_to_class('friendly_urls', generic.GenericRelation(UrlMapping))


This basically monkey patches the User model to add a field. You can then do

user = User.objects.get(pk=1)
user.friendly_urls.all()

to get a list of all the friendly urls.

Problems / Questions
--------------------

Don't forget to run syncdb because friendlyurls creates tables.


