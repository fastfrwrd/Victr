from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('victr.api.views',
    url(r'^project', 'project', name='project'),
    url(r'^project/(?P<slug>.+)$', 'project_id', name='project_id'),
)