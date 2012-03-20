from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('victr.project.views',
    url(r'^/new/$', 'new', name='victr_project_new'),
    url(r'^/(?P<slug>.+)/edit/$', 'edit', name='victr_project_edit'),
    url(r'^/(?P<slug>.+)/$', 'project', name='victr_project_project'),
)