from django.db import models
from django.contrib.auth.models import User
from places.models import Place, Attraction
from experiences.models import Experience, Trip
from users.models import Profile
from geoposition.fields import GeopositionField
from django.utils import timezone


# Create your models here.



class Booking (models.Model):

    slug = models.SlugField(max_length=128, unique=True, default='null')
    commment = models.TextField(max_length=256, null=True)
    date_booked = models.DateTimeField(default=timezone.now(), null=True, blank=True)
    total_price = models.IntegerField(default=0)
    customer_cnic = models.TextField(max_length=256, blank=True, null=True)	
    customer_phone_number = models.TextField(max_length=256, blank=True, null=True)
    customer_email = models.EmailField(('email address'), max_length=256, blank=True)
    customer_slug = models.ForeignKey(User, unique=True, on_delete=models.PROTECT)

    
    class Meta:
        abstract = True

    def __str__(self):
        return self.slug




class TripBooking (Booking):
    guest_number = models.IntegerField(max_length=256, default=1)
    phone_number = models.TextField(max_length=256, default='null')
    email_id = models.EmailField(max_length=256, default='null')
    booked_trip = models.ForeignKey(Trip, on_delete=models.PROTECT)


    def __str__(self):
        return self.slug

class ExperienceBooking (Booking):
    guest_number = models.IntegerField(max_length=256, default=1)
    phone_number = models.TextField(max_length=256, default='null')
    email_id = models.EmailField(max_length=256, default='null')
    booked_experience = models.ForeignKey(Experience, on_delete=models.PROTECT)


    def __str__(self):
        return self.slug
