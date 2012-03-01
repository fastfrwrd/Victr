# Victr #

a tool to manage your competitions (like hack days!)
by Tucker Bickler, Paul Marbach, Raul Mireles, and Shela Xu

_coming soon to a GitHub near you_

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
    
5.  follow the Manual configs below

## Manual configs: ##
#### settings.py: ####
_this needs to map to your the url you set in urls.py_

    LOGIN_URL = '/victr/auth/login'
    LOGOUT_URL = '/victr/auth/logout'
    LOGIN_REDIRECT_URL = '/victr/'

    INSTALLED_APPS = (
        ... #your other apps are above this
        'victr', #boom
        'django.contrib.admin', #to edit and add events
        ... #other apps, your victr extension
    )
        
    import django.conf.global_settings as DEFAULT_SETTINGS
    TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
        'django.core.context_processors.request',
    )

#### urls.py ####

    urlpatterns = patterns('',
        #this points to http://yoursiteurl.com/victr/. you can do root if you want too with the pattern r'^'
        url(r'^victr/', include('victr.urls')),
        ...
        # Uncomment the next line to enable the admin:
        url(r'^admin/', include(admin.site.urls)),
    )

## Dependencies ##
pil (for thumbnail images)

    $ > pip install pil

## Testing procedures ##
#### dump fixtures ####

    $ > python manage.py dumpdata --exclude=auth --exclude=contenttypes > apps/victr/fixtures/initial_data.json  

#### install fixtures ####

    $ > python manage.py reset victr  
    $ > python manage.py syncdb
