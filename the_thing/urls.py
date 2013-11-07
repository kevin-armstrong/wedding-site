from django.conf.urls import patterns, url

from the_thing import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^directions/$', views.directions, name='directions'),
    url(r'^fun_stuff/$', views.fun_stuff, name='fun_stuff'),
    url(r'^rsvp/$', views.rsvp, name='rsvp'),
    url(r'^login/(?P<username>\w*)$', views.login, name='login'),
    
    url(r'^logout$', views.logout, name='logout'),
    url(r'^(?P<user_id>\d+)/response/$', views.response, name='response')
    
)