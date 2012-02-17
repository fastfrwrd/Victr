from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('victr.views',
	url(r'^$', 'home', name='home'),
    url(r'^project/new', 'project_new', name='project_new'),
    url(r'^project/(?P<slug>.+)$', 'project_view', name='project_view'),
	url(r'^impress/', include('victr.impress.urls')),
)
