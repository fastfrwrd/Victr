from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('victr.project.views',
    url(r'^/all$', 'all', name='all'),
    url(r'^/new$', 'new', name='new'),
    url(r'^/(?P<slug>.+)/edit$', 'edit', name='edit'),
    url(r'^/(?P<slug>.+)$', 'project', name='project'),
)