# Victr #

a tool to manage your competitions (like hack days!)

by Tucker Bickler, Paul Marbach, Raul Mireles, and Shela Xu

_coming soon to a GitHub Near you_

### "to the victr go the spoils" ###

## Manual configs: ##

#### settings.py: ####
    LOGIN_URL = '/login/'
_this can be whatever you want, we think login makes sense if you're installing Victr at your root URL_

    INSTALLED_APPS = (
        ...
        'victr',
        ...
    )

#### urls.py ####

    urlpatterns = patterns('',
        # ONE OF THESE TWO can be used to get to victr
        # url(r'^', include('victr.urls')), #NO trailing $! this points to http://yoursitesurl.com/
        # url(r'^victr/', include('victr.urls')), #this points to http://yoursiteurl.com/victr
    )

#### dump fixtures ####
python manage.py dumpdata --exclude=auth --exclude=contenttypes > victr/fixtures/initial_data.json  

#### install fixtures ####
python manage.py reset victr  
python manage.py syncdb  
