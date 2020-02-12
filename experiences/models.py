from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from places.models import Place
from places.models import Attraction
from polymorphic.models import PolymorphicModel
from django.utils import timezone   

# Create your models here.


class Category(models.Model):
    slug = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=128)
    image = models.ImageField(null=True, upload_to='experience_images/category_covers')

    def __str__(self):
        return self.slug

class Package(models.Model):
    slug = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=128)
    image = models.ImageField(null=True, upload_to='experience_images/category_covers')

    def __str__(self):
        return self.slug


class Base (models.Model):
    category = models.ManyToManyField(Category, blank=True, related_name="%(app_label)s_%(class)s_related",
                                      related_query_name="%(app_label)s_%(class)ss",
                                        )
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=128, unique=True, default='null')
    overview = models.TextField()
    date_booked = models.DateTimeField(default=timezone.now(), null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name="%(app_label)s_%(class)s_related",
                                      related_query_name="%(app_label)s_%(class)ss",
                                        )
    image = models.ImageField(null=True, blank=True, upload_to='experience_images')
    location = models.ManyToManyField(Place, blank=True, related_name="%(app_label)s_%(class)s_related",
                                      related_query_name="%(app_label)s_%(class)ss",
                                        )
    price = models.IntegerField(default=0)
    gallery = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.slug


class Experience(Base):

    itinerary = models.TextField(null=True, blank=True)
    host = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    attractions = models.ManyToManyField(Attraction, blank=True)
    package_choice = [('P', 'Public'), ('E', 'Exclusive')]

    def __str__(self):
        return self.slug


class Trip (Base):
    start_date = models.DateTimeField(default=timezone.now(), null=True, blank=True)
    end_date = models.DateTimeField(default=timezone.now(), null=True, blank=True)
    itinerary = models.TextField(null=True, blank=True)
    host = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    experiences = models.ManyToManyField(Experience, blank=True)
    attractions = models.ManyToManyField(Attraction, blank=True)
    package_choice = [('S', 'Single Occupancy'), ('D', 'Double Occupancy'), ('C', 'Custom for 10 people'), ('T', 'Both Triple and Quad Occupancy')]

    def __str__(self):
        return self.slug






