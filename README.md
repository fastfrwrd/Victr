# Victr #

a tool to manage your competitions (like hack days!)

by Tucker Bickler, Paul Marbach, Raul Mireles, and Shela Xu

_coming soon to a GitHub Near you_

### "to the victr go the spoils" ###

## Suggested installation procedure: ##
_just a suggested approach to get you up and Victr-ing - there are other possible methods_
1. create a new django project with `django-admin.py startproject mysite`
2. create an apps folder `cd mysite && mkdir apps && touch ./apps/__init.py__`
3. clone Victr into the apps folder
4. add the following to settings.py:
    import os
    import sys

    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

## Manual configs: ##
#### settings.py: ####
    LOGIN_URL = '/victr/login/'
    LOGOUT_URL = '/victr/logout/'
    LOGIN_REDIRECT_URL = '/victr/'
_this needs to map to your victr folder (which can be root)_

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

#### dump fixtures ####
python manage.py dumpdata --exclude=auth --exclude=contenttypes > victr/fixtures/initial_data.json  

#### install fixtures ####
python manage.py reset victr  
python manage.py syncdb  
