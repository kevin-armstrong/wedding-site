from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

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
    return HttpResponseRedirect(reverse('index'))