# Victr #

a tool to manage your competitions (like hack days!)

by Tucker Bickler, Paul Marbach, Raul Mireles, and Shela Xu

_coming soon to a GitHub Near you_

### "to the victr go the spoils" ###

## Suggested installation procedure: ##

1.  create a new django project with `django-admin.py startproject mysite`
2.  create an apps folder `cd mysite && mkdir apps && touch ./apps/__init.py__`
3.  clone Victr into the apps folder
4.  add the following to settings.py:

    import os
    import sys

    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
5.  folow the Manual configs below

## Manual configs: ##
#### settings.py: ####
_this needs to map to your the url you set in urls.py_

    LOGIN_URL = '/victr/login/'
    LOGOUT_URL = '/victr/logout/'
    LOGIN_REDIRECT_URL = '/victr/'

    INSTALLED_APPS = (
        ...
        'victr',
        ...
    )

#### urls.py ####

    urlpatterns = patterns('',
        url(r'^victr/', include('victr.urls')), #this points to http://yoursiteurl.com/victr/. you can do root if you want too with the pattern r'^'
        ...
    )

## Testing procedures ##
#### dump fixtures ####
    $ > python manage.py dumpdata --exclude=auth --exclude=contenttypes > victr/fixtures/initial_data.json  

#### install fixtures ####
    $ > python manage.py reset victr  
    $ > python manage.py syncdb  
