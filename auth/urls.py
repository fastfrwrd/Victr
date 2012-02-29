from django.conf.urls.defaults import patterns, include, url
#
urlpatterns = patterns('victr.auth.views',
    url(r'^/register/$'       , 'register'      , name='register'      ),
    url(r'^/register/modal/$' , 'register_modal', name='register_modal'),
    url(r'^/login/$'          , 'login'         , name='login'         ),
    url(r'^/login/nav/$'      , 'login_nav'     , name='login_nav'     ),
    url(r'^/logout/$'         , 'logout'        , name='logout'        ),
    url(r'^/user/$'           , 'profile'       , name='profile'       ),
    url(r'^/user/(?P<id>.+)/$', 'profile'       , name='profile'       ),
)
