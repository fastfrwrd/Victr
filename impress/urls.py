from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('victr.impress.views',
	url(r'^/$', 'present', name='victr_impress_present'),
	url(r'^/present/$', 'present', name='victr_impress_present'),
	url(r'^/present/(?P<slug>.+)/$', 'present', name='victr_impress_present'),
)