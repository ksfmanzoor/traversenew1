from django.db import models
from geoposition.fields import GeopositionField
from taggit.managers import TaggableManager


class Region(models.Model):
    slug = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.slug


class Category(models.Model):
    slug = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.slug


class Type(models.Model):
    slug = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.slug


class Attraction(models.Model):
    slug = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=256)
    coverImage = models.CharField(max_length=256)
    description = models.TextField()
    gettingThere = models.TextField()
    featured = models.BooleanField()
    location = GeopositionField()
    gallery = models.CharField(max_length=256, null=True, blank=True)
    place = models.ManyToManyField('Place', blank=True)

    def __str__(self):
        return self.slug


class Place(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    type = models.ManyToManyField(Type, blank=True)
    slug = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=256)
    coverImage = models.CharField(max_length=256)
    description = models.TextField()
    gettingThere = models.TextField()
    featured = models.BooleanField()
    location = GeopositionField()
    tags = TaggableManager()
    gallery = models.CharField(max_length=256, null=True, blank=True)
    # attraction = models.ManyToManyField(Atrraction, related_name='attractions', blank=True)
    # attractions = models.ManyToOneRel(Atrraction, to=Atrraction, field_name='place')

    def __str__(self):
        return self.slug



