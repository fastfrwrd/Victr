from django.conf.urls.defaults import patterns, include, url
#
urlpatterns = patterns('victr.auth.views',
    url(r'^/register/$'       , 'register'      , name='victr_auth_register'      ),
    url(r'^/register/modal/$' , 'register_modal', name='victr_auth_registermodal'),
    url(r'^/login/$'          , 'login'         , name='victr_auth_login'         ),
    url(r'^/login/nav/$'      , 'login_nav'     , name='victr_auth_loginnav'     ),
    url(r'^/logout/$'         , 'logout'        , name='victr_auth_logout'        ),
    url(r'^/user/$'           , 'profile'       , name='victr_auth_profile'       ),
    url(r'^/user/edit/$'      , 'edit'          , name='victr_auth_edit'          ),
    url(r'^/user/(?P<id>.+)/$', 'profile'       , name='victr_auth_profile'       ),
)
