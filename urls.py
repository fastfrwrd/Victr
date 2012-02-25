from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'victr.views.home'),
    url(r'api', include('victr.api.urls')),
    url(r'project', include('victr.project.urls')),
    url(r'impress', include('victr.impress.urls')),
    url(r'event', include('victr.event.urls')), 
    #temporary: below are the patterns as they appear in main/urls.py for the auth work
    url(r'register/$', 'victr.views.register'), #temporary login work
    url(r'login/$', 'victr.views.login'), #temporary login work
    url(r'logout/$', 'victr.views.logout'), #temporary login work
)
