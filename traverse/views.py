from django.shortcuts import render
from places.models import Category, Region, Place


def about(request):
    return render(request, 'about.html')


def index(request):
    places = list(Place.objects.filter(featured=True))
    context_dict = {
        'categories': Category.objects.all(),
        'regions': Region.objects.all(),
        'featured_places': places
    }
    return render(request, 'home.html', context_dict)
