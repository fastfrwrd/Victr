from django.conf.urls import patterns, include, url

urlpatterns = patterns('victr.views',
    url(r'^$', 'index'),
)
