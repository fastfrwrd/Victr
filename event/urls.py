from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('victr.event.views',
    url(r'^/$', 'view', name='view'),
	url(r'^/(?P<slug>.+)/$', 'view', name='view'),
)