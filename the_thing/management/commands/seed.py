from django.core.management.base import NoArgsCommand, CommandError
from the_thing.models import Guest

class Command(NoArgsCommand):
    help = "Seeds the guest list data"
    
    def handle_noargs(self, **options):
        guest_list = [
            Guest(name ="Tomo Takaki", invited_to_brunch = True, invited_to_rehersal_dinner = False),
            Guest(name ="Shirley Liou", invited_to_brunch = True, invited_to_rehersal_dinner = False),
            Guest(name ="Greg & Angela Rozmyn", invited_to_brunch = True, invited_to_rehersal_dinner = False),
            Guest(name ="Stefanie Morris", invited_to_brunch = True, invited_to_rehersal_dinner = False),
            Guest(name ="Eunice Yoon & Herman Marcia", invited_to_brunch = True, invited_to_rehersal_dinner = False),
            Guest(name ="Michael Ostertag", invited_to_brunch = True, invited_to_rehersal_dinner = False),
            Guest(name ="Chase Cross", invited_to_brunch = True, invited_to_rehersal_dinner = False),
            Guest(name ="Kathleen Walkley & Nicholas Pettinati", invited_to_brunch = True, invited_to_rehersal_dinner = True),
            Guest(name ="Melissa Lumish & Guest", invited_to_brunch = True, invited_to_rehersal_dinner = True),
            Guest(name ="Megan & Jared Scott", invited_to_brunch = True, invited_to_rehersal_dinner = True),
            Guest(name ="Rebecca (Zellner) & Daniel Youngblut", invited_to_brunch = True, invited_to_rehersal_dinner = True),
            Guest(name ="Ethan Benanav & Mandy Heiser", invited_to_brunch = True, invited_to_rehersal_dinner = False),
            Guest(name ="Benjamin Eisen & Emily Cohn", invited_to_brunch = False, invited_to_rehersal_dinner = False),
            Guest(name ="Will Hui", invited_to_brunch = True, invited_to_rehersal_dinner = False),
            Guest(name ="Kan Yang & Carolina Dulcey", invited_to_brunch = True, invited_to_rehersal_dinner = False),
            Guest(name ="Ms. Shan Li & Mr. Jin Fang", invited_to_brunch = True, invited_to_rehersal_dinner = True),
            Guest(name ="Daniel Fang & Alex Minsk", invited_to_brunch = True, invited_to_rehersal_dinner = True),
            Guest(name ="Ms. Lu Yan Yuen & Mr. Jim Tarzia", invited_to_brunch = True, invited_to_rehersal_dinner = False),
            Guest(name ="Charlotte Chen", invited_to_brunch = True, invited_to_rehersal_dinner = False),
            Guest(name ="Torey Alford", invited_to_brunch = True, invited_to_rehersal_dinner = False),
            Guest(name ="Matthew Tolson", invited_to_brunch = True, invited_to_rehersal_dinner = False),
            Guest(name ="Ian Duckworth & Hope Newton", invited_to_brunch = True, invited_to_rehersal_dinner = False),
            Guest(name ="Bin Zhou & Joanna Kim", invited_to_brunch = True, invited_to_rehersal_dinner = False),
            Guest(name ="Bruce & Nancy Lumish", invited_to_brunch = True, invited_to_rehersal_dinner = True),
            Guest(name ="Sarah Zhang & Gene Eline", invited_to_brunch = False, invited_to_rehersal_dinner = False),
            Guest(name ="Eric, Kathy, Tyler & Ryan Watson", invited_to_brunch = True, invited_to_rehersal_dinner = False),
            Guest(name ="Ian Nimblett & Nicole Root", invited_to_brunch = False, invited_to_rehersal_dinner = False),
            Guest(name ="Clay Viands & Kris McIntyre", invited_to_brunch = False, invited_to_rehersal_dinner = True),
            Guest(name ="Lukasz & Valerie Strozek", invited_to_brunch = True, invited_to_rehersal_dinner = False),
            Guest(name ="Zain Khalid & Saba Sulaiman", invited_to_brunch = False, invited_to_rehersal_dinner = False),
            Guest(name ="Timothy & Laurie Miller", invited_to_brunch = False, invited_to_rehersal_dinner = False),
            Guest(name ="Harry Tian & Yan Wen Jun", invited_to_brunch = False, invited_to_rehersal_dinner = False),
            Guest(name ="Gideon & Jana Romm", invited_to_brunch = True, invited_to_rehersal_dinner = False),
            Guest(name ="Claude & Jennifer Amadeo", invited_to_brunch = False, invited_to_rehersal_dinner = False),
            Guest(name ="Joel Thompson", invited_to_brunch = False, invited_to_rehersal_dinner = False),
            Guest(name ="Lawrence Mark & His Hot Wife", invited_to_brunch = False, invited_to_rehersal_dinner = False),
            Guest(name ="Ian Leue & Sarah Hartshorne", invited_to_brunch = False, invited_to_rehersal_dinner = False),
            Guest(name ="Todd & Sarah Kuhns", invited_to_brunch = False, invited_to_rehersal_dinner = False),
            Guest(name ="Jarrod Luchsinger & Marci Kington", invited_to_brunch = False, invited_to_rehersal_dinner = False),
            Guest(name ="Thomas & Nicole Steinthal", invited_to_brunch = True, invited_to_rehersal_dinner = True),
            Guest(name ="Nolan Salisbury & Nathalie Nucho", invited_to_brunch = False, invited_to_rehersal_dinner = False),
            Guest(name ="Kristoffer & Erin Singleton", invited_to_brunch = False, invited_to_rehersal_dinner = False),
            Guest(name ="Hassan Sultan", invited_to_brunch = True, invited_to_rehersal_dinner = False),
            Guest(name ="Stephen Mokszycki", invited_to_brunch = False, invited_to_rehersal_dinner = False),
            Guest(name ="Vivian Lai & Ryan Youngsaye", invited_to_brunch = False, invited_to_rehersal_dinner = False),
            Guest(name ="Mr. & Mrs. Edward W. Armstrong", invited_to_brunch = True, invited_to_rehersal_dinner = True),
            Guest(name ="Brad & Toni Armstrong", invited_to_brunch = True, invited_to_rehersal_dinner = True),
            Guest(name ="George Price & Rodney McManus", invited_to_brunch = True, invited_to_rehersal_dinner = True),
            Guest(name ="Gregory Price & Vicki Coleman", invited_to_brunch = True, invited_to_rehersal_dinner = True),
            Guest(name ="Gretchen & Cliff Horton", invited_to_brunch = True, invited_to_rehersal_dinner = True),
            Guest(name ="Emily Horton", invited_to_brunch = False, invited_to_rehersal_dinner = True),
            Guest(name ="Elizabeth Horton & Hayden Horton", invited_to_brunch = True, invited_to_rehersal_dinner = True),
            Guest(name ="Mrs. Betty Price", invited_to_brunch = True, invited_to_rehersal_dinner = True),
            Guest(name ="Ms. Deb Walters", invited_to_brunch = True, invited_to_rehersal_dinner = True),
            Guest(name ="Dr. & Mrs. Robert B. Armstrong", invited_to_brunch = True, invited_to_rehersal_dinner = True),
            Guest(name ="Andrew Armstrong", invited_to_brunch = True, invited_to_rehersal_dinner = True),
            Guest(name ="Reed Armstrong", invited_to_brunch = True, invited_to_rehersal_dinner = True),
            Guest(name ="Dr. & Mrs. Walter R. Graham", invited_to_brunch = True, invited_to_rehersal_dinner = True),
        ]

        already_imported_guests = 0
        newly_imported_guests = 0
        for guest in guest_list:
            already_saved_guest = Guest.objects.filter(name__iexact=guest.name)
            if already_saved_guest:
                already_imported_guests += 1
            else:
                newly_imported_guests += 1
                guest.save()
        
        print("Imported {0} new guest(s). Skipped {1} existing guest(s).".format(newly_imported_guests, already_imported_guests))
