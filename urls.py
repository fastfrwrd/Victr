from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'victr.views.home'),
    url(r'api', include('victr.api.urls')),
    url(r'project', include('victr.project.urls')),
    url(r'impress', include('victr.impress.urls')),
    url(r'event', include('victr.event.urls')),
    url(r'auth', include('victr.auth.urls')),
    
    #todo: move below patterns into subapp
    url(r'archive/$', 'victr.views.archive'),
)
