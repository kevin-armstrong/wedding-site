from django.db import models

class Guest(models.Model):
    name = models.CharField(max_length=200)
    number_of_guests = models.IntegerField(default=0)
    
    will_attend = models.NullBooleanField()
    invited_to_brunch = models.BooleanField(default=False)
    will_attend_brunch = models.NullBooleanField()
    invited_to_rehersal_dinner = models.BooleanField(default=False)
    will_attend_rehersal_dinner = models.NullBooleanField()

    dietary_restrictions = models.TextField()

    def __str__(self):
        return self.name
