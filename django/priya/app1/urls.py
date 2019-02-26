from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     url(r'^home/$', views.home, name='home'),
     url(r'^$', views.index, name='index'),
     url(r'^login/$', views.login1, name='login1'),
     url(r'^course/$', views.courses, name='courses'),
    url(r'^aboutus/$', views.about, name='about'),
    url(r'^contact/$', views.contactus, name='contactus'),
    url(r'^registration/$', views.regform, name='regform'),
     url(r'^logout/$',auth_views.logout,{'next_page': 'login1'}, name='logout'),
     url(r'^get_result/$', views.response, name='response'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

]