from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', include('victr.event.urls')),
    url(r'^api', include('victr.api.urls')),
    url(r'^project', include('victr.project.urls')),
    url(r'^impress', include('victr.impress.urls')),
    url(r'^login/$', 'victr.views.login'),
    #temporary: below are the patterns as they appear in main/urls.py for the auth work
    (r'register/$', 'victr.views.register'), #temporary login work
    (r'login/$', 'victr.views.login'), #temporary login work
    (r'vip/$', 'victr.views.vip'), #temporary login work
    (r'logout/$', 'victr.views.logout'), #temporary login work
)
