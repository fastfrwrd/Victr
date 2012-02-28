from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('victr.impress.views',
	url(r'^/$', 'present', name='present'),
	url(r'^/present/$', 'present', name='present'),
	url(r'^/present/(?P<slug>.+)/$', 'present', name='present'),
)