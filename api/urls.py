from django.conf.urls.defaults import patterns, include, url
#
urlpatterns = patterns('victr.api.views',
    url(r'^/discipline/search/(?P<slug>.+)/$', 'discipline_search', name='discipline_search'),
)
