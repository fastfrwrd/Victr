from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('victr.event.views',
	url(r'^/list$', 'list', name='list'),
)