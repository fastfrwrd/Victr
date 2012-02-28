from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('victr.event.views',
    url(r'^/$', 'view', name='view'),
	url(r'^/all/$', 'all', name='all'),
	url(r'^/results/$', 'results', name='results'),
	url(r'^/(?P<slug>.+)/$', 'view', name='view'),
	url(r'^/results/(?P<slug>.+)/$', 'results', name='results'),
)