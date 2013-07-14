from django.conf.urls import patterns, url

from the_thing import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>\d+)/rsvp/$', views.rsvp, name='rsvp'),
    url(r'^(?P<user_id>\d+)/response/$', views.response, name='response')
)