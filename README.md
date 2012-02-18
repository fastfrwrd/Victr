# Victr #

a tool to manage your hackathons (and other competitions in general)
by Tucker Bickler, Paul Marbach, Raul Mireles, and Shela Xu

_coming soon to a GitHub Near you_

### "to the victr go the spoils" ###

## Manual configs: ##

#### settings.py: ####
`LOGIN_URL = '/login/'`
_this can be whatever you want, we think login makes sense if you're installing Victr at your root URL_

`INSTALLED_APPS = (
    ...
    'victr',
    ...
)`

#### urls.py ####

`urlpatterns = patterns('',
    # ONE OF THESE TWO can be used to get to victr
    # url(r'^', include('victr.urls')), #NO trailing $! this points to http://yoursitesurl.com/
    # url(r'^victr/', include('victr.urls')), #this points to http://yoursiteurl.com/victr
)`