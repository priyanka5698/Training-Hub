from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     url(r'^home/$', views.home, name='home'),
     url(r'^$', views.index, name='index'),
     url(r'^login/$', views.login1, name='login1'),
     url(r'^registration/$', views.regform, name='regform'),
     url(r'^logout/$',auth_views.logout,{'next_page': 'login1'}, name='logout'),
     url(r'^get_result/', views.response, name='response'),

]