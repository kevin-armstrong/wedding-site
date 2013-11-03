from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from smtplib import SMTP_SSL

from the_thing.models import Guest

def index(request):
    all_guests = Guest.objects.all()
    template = loader.get_template('the_thing/index.html')
    context = RequestContext( request, {
        'all_guests': all_guests,
    })
    return HttpResponse(template.render(context))

def will_attend(request, user_id):
    guest = Guest.objects.get(id=user_id)
    return HttpResponse("The user name is %s." % guest.name)
    

def rsvp(request, user_id):
    guest = Guest.objects.get(id=user_id)
    template = loader.get_template('the_thing/rsvp.html')
    context = RequestContext( request, {
        'guest': guest,
    })
    return HttpResponse(template.render(context))
    
def response(request, user_id):
    guest = Guest.objects.get(id=user_id)
    will_attend_string = request.POST['will_attend']
    guest.will_attend = True if will_attend_string == "yes" else False

    guest.number_of_guests = request.POST['number_of_guests']
    guest.save()
    
    #uncomment in production
    #send_email_notification(guest)
    
    if guest.name == "Tim Miller":
        return HttpResponseRedirect('http://www.youtube.com/watch?v=dQw4w9WgXcQ')
        
    return HttpResponseRedirect(reverse('index'))

def directions(request):
    template = loader.get_template('the_thing/directions.html')
    context = RequestContext( request )
    return HttpResponse(template.render(context))
    
def fun_stuff(request):
    template = loader.get_template('the_thing/fun_stuff.html')
    context = RequestContext( request )
    return HttpResponse(template.render(context))

def send_email_notification(guest):
    smtp_server_name = "smtp.gmail.com"
    smtp_username = "theshortestnameavailable@gmail.com"
    smtp_password = "W3dding_"
    
    to_address = "kevin.t.armstrong@gmail.com"
    message = make_message(guest)
    smtp_server = SMTP_SSL(smtp_server_name)
    smtp_server.login(smtp_username, smtp_password)
    smtp_server.sendmail("from", to_address, message)
    smtp_server.quit()
    
    return
    
def make_message(guest):
    response = "yes" if guest.will_attend else "no"
    message_body = guest.name + " just RSVPed " + response + ", with " + guest.number_of_guests + " guests."
    
    message = """From: Wedding Site
To: Kevin Armstrong <kevin.t.armstrong@gmail.com>
Subject: RSVP from """ + guest.name + "\n\n" + message_body
    
    return message
