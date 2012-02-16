from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('victr.views',
	url(r'^$', 'home', name='home'),
	url(r'^hack/new', 'hack_new', name='hack_new'),
)
