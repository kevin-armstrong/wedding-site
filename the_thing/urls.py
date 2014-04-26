from django.conf.urls import patterns, url

from the_thing import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^fairfield/$', views.fairfield, name='fairfield'),
	url(r'^nyc/$', views.nyc, name='nyc'),
	url(r'^wedding_party/$', views.wedding_party, name='wedding_party'),
    url(r'^fun_stuff/$', views.fun_stuff, name='fun_stuff'),
    url(r'^location/$', views.location, name='location'),
	url(r'^itinerary/$', views.itinerary, name='itinerary'),
	url(r'^brunch/$', views.brunch, name='brunch'),
	url(r'^rehearsal/$', views.rehearsal, name='rehearsal'),
    url(r'^rsvp/$', views.rsvp, name='rsvp'),
	url(r'^view_guests/$', views.view_guests, name='view_guests'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^(?P<user_id>\d+)/response/$', views.response, name='response'),
    url(r'^get_attendees$', views.get_attendees, name='get_attendees'),
    url(r'^perform_login$', views.perform_login, name='perform_login')
)