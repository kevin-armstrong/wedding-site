from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from smtplib import SMTP_SSL
import inspect, string
import json

from the_thing.models import Guest

def index(request):
    all_guests = Guest.objects.all()
    current_function_name = _get_calling_method_name()
    
    return _render_template(request, current_function_name, { 'all_guests': all_guests })

def rsvp(request):
    user_id = request.session.get('user_id','')
    if user_id:
        guest = Guest.objects.get(id=user_id)
        current_function_name = _get_calling_method_name()
        return _render_template(request, current_function_name, { 'guest': guest })

    return _render_template(request, 'login', {})

def login(request):
    current_function_name = _get_calling_method_name()
    return _render_template(request, current_function_name, {})

def perform_login(request):
    user_id = request.POST['login_id']
    request.session['user_id'] = user_id
 
    return HttpResponseRedirect(reverse('rsvp'))
    
def logout(request):
    request.session.clear()
    return _render_template(request, 'index', {})    

def response(request, user_id):
    guest = Guest.objects.get(id=user_id)
    will_attend_string = request.POST['will_attend']
    guest.will_attend = True if will_attend_string == "yes" else False

    if "will_attend_brunch" in request.POST:
        guest.will_attend_brunch = True if request.POST['will_attend_brunch'] == "yes" else False
    
    if "will_attend_rehersal_dinner" in request.POST:
        guest.will_attend_rehersal_dinner = True if request.POST['will_attend_rehersal_dinner'] == "yes" else False

    guest.number_of_guests = request.POST['number_of_guests']
    guest.dietary_restrictions = request.POST['dietary_restrictions']
    guest.save()
    
    #uncomment in production
    #_send_email_notification(guest)
    
    if guest.name == "Tim Miller":
        return HttpResponseRedirect('http://www.youtube.com/watch?v=dQw4w9WgXcQ')
        
    return HttpResponseRedirect(reverse('index'))

def fairfield(request):
	return _render_static_content(request, _get_calling_method_name())

def nyc(request):
	return _render_static_content(request, _get_calling_method_name())

def itinerary(request):
	return _render_static_content(request, _get_calling_method_name())

def rehearsal(request):
	return _render_static_content(request, _get_calling_method_name())

def brunch(request):
	return _render_static_content(request, _get_calling_method_name())

def location(request):
	return _render_static_content(request, _get_calling_method_name())
    
def fun_stuff(request):
	return _render_static_content(request, _get_calling_method_name())

def wedding_party(request):
	return _render_static_content(request, _get_calling_method_name())

def get_attendees(request):
    search_term = request.GET.get('searchTerm')
    
    guests = Guest.objects.all()
    search_terms = search_term.split(' ')
    for term in search_terms:
        guests = guests.filter(name__iregex=r"\b" + term)
    
    guest_names = list(map(lambda g: {"id": g.id, "text": g.name}, guests))

    return HttpResponse(json.dumps(guest_names), content_type="application/json")
    
def _render_static_content(request, page_name):
    return _render_template(request, page_name, {})

def _render_template(request, function_name, parameter_dictionary):
    parameter_dictionary['page_title'] = _make_pretty_name(function_name)
    template_name = 'the_thing/' + function_name + '.html'
    template = loader.get_template(template_name)
    context = RequestContext(request, parameter_dictionary)
    return HttpResponse(template.render(context))

def _make_pretty_name(function_name):
    pretty_function_name = string.capwords(function_name.replace('_', ' '))
    return pretty_function_name

def _get_calling_method_name():
    return inspect.stack()[1][3]
	
def _send_email_notification(guest):
    smtp_server_name = "smtp.gmail.com"
    smtp_username = "theshortestnameavailable@gmail.com"
    smtp_password = "W3dding_"
    
    to_address = "kevin.t.armstrong@gmail.com"
    message = _make_message(guest)
    smtp_server = SMTP_SSL(smtp_server_name)
    smtp_server.login(smtp_username, smtp_password)
    smtp_server.sendmail("from", to_address, message)
    smtp_server.quit()
    
    return
    
def _make_message(guest):
    response = "yes" if guest.will_attend else "no"
    message_body = guest.name + " just RSVPed " + response + ", with " + guest.number_of_guests + " guests. Dietary restrictions: " + guest.dietary_restrictions
    
    message = """From: Wedding Site
To: Kevin Armstrong <kevin.t.armstrong@gmail.com>
Subject: RSVP from """ + guest.name + "\n\n" + message_body
    
    return message
