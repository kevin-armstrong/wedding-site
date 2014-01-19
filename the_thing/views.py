from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from smtplib import SMTP_SSL
import inspect, string

from the_thing.models import Guest

def index(request):
    all_guests = Guest.objects.all()
    current_function_name = _get_calling_method_name()
    
    return _render_template(request, current_function_name, { 'all_guests': all_guests })

def rsvp(request):
    username = request.session.get('user','')
    if username:
        #TODO: probably improve the matching logic
        guests = Guest.objects.filter(name__startswith=username)
        if guests:
            #TODO: only match one guest?
            guest = guests[0]
            current_function_name = _get_calling_method_name()
            return _render_template(request, current_function_name, { 'guest': guest })
    
    return _render_static_content(request, 'login_required')

def login(request, username):
    if username:
        request.session['user'] = username
 
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

def location(request):
	return _render_static_content(request, _get_calling_method_name())
    
def fun_stuff(request):
	return _render_static_content(request, _get_calling_method_name())

def wp_groom(request):
	return _render_static_content(request, _get_calling_method_name())
	
def wp_bride(request):
	return _render_static_content(request, _get_calling_method_name())

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
