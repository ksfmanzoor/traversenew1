from django.contrib import admin
from .models import Category, Region, Place, Attraction, Type


admin.site.register(Category)
admin.site.register(Region)
admin.site.register(Place)
admin.site.register(Attraction)
admin.site.register(Type)
