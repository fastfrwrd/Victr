from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('victr.views',
	url(r'^$', include('victr.event.urls'), name='current'),
    url(r'^project/', include('victr.project.urls')),
    url(r'^impress/', include('victr.impress.urls')),
)
