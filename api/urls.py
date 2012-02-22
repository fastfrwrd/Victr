from django.conf.urls.defaults import patterns, include, url
#
urlpatterns = patterns('victr.api.views',
#    url(r'^(?P<object>.+)/(?P<slug>.+)/$', 'rest_id', name='rest_id'),
#    url(r'^(?P<object>.+)/(?P<slug>.+)$', 'rest_id', name='rest_id'),
#    url(r'^(?P<object>.+)/$', 'rest', name='rest'),
#    url(r'^(?P<object>.+)$', 'rest', name='rest'),
##    url(r'^project$', 'project', name='project'),
##    url(r'^project/(?P<slug>.+)$', 'project_id', name='project_id'),
    url(r'^/discipline/search/(?P<slug>.+)$', 'discipline_search', name='discipline_search'),
)
