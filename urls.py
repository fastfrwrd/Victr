from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', include('victr.event.urls')),
    url(r'^api', include('victr.api.urls')),
    url(r'^project', include('victr.project.urls')),
    url(r'^impress', include('victr.impress.urls')),
    url(r'^login/$', 'victr.views.login')                        
)
