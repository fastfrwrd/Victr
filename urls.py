from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('victr.views',
	url(r'^$', 'home', name='home'),
	url(r'^project/new', 'project_new', name='project_new'),
	url(r'^impress/present', 'impress_present', name='impress_present'),
)
