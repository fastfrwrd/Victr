from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('victr.event.views',
	url(r'^$', 'current', name='current'),
	url(r'^list$', 'current', name='list'),
)