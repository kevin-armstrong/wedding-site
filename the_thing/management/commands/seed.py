from django.core.management.base import NoArgsCommand, CommandError
from the_thing.models import Guest

class Command(NoArgsCommand):
    help = "Seeds the guest list data"
    
    def handle_noargs(self, **options):
        guest_list = ["Brad Armstrong", "Clay Viands", "Tim Miller", "Shan Li", "Bill Armstrong"]
        #, "George Price", "Gregory Price", "Gretchen Horton", "Betty Price", "Bob Armstrong", "Cynthia Graham",
        #"Kris Singleton", "Nolan Salisbury", "Tom Steinthal", "Todd Kuhns", "Ian Leue", "Larry Mark"]

        already_imported_guests = 0
        newly_imported_guests = 0
        for guest_name in guest_list:
            guest = Guest.objects.filter(name__iexact=guest_name)
            if guest:
                already_imported_guests += 1
            else:
                newly_imported_guests += 1
                guest = Guest(name = guest_name)
                guest.save()
        
        print("Imported {0} new guest(s). Skipped {1} existing guest(s).".format(newly_imported_guests, already_imported_guests))
