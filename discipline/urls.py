from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('victr.discipline.views',
    url(r'^/(?P<slug>.+)/$', 'view', name='view'),
)