from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('victr.event.views',
    url(r'^/$', 'view', name='victr_event_view'),
	url(r'^/(?P<slug>.+)/$', 'view', name='victr_event_view'),
)