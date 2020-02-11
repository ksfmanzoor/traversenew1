from django.db import models
from places.models import Place
from geoposition.fields import GeopositionField

# Create your models here.


class Hotel(models.Model):

    slug = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=256)
    coverImage = models.CharField(max_length=256)
    description = models.TextField()
    gettingThere = models.TextField()
    featured = models.BooleanField()
    location = GeopositionField()
    gallery = models.CharField(max_length=256, null=True, blank=True)
    place = models.ManyToManyField(Place, blank=True)

    def __str__(self):
        return self.slug

