import os
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.forms.models import model_to_dict
from django.db.models import Q
from sorl.thumbnail import get_thumbnail

from .models import Place, Category, Region, Attraction, Type
from taggit.models import Tag
from experiences.models import Experience, Trip
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import get_object_or_404, get_list_or_404
from blog.models import Post
from django.db.models import prefetch_related_objects


def index(request):
    context_dict = {
        'categories': Category.objects.all(),
        'regions': Region.objects.all()
    }

    return render(request, 'places/home.html', context_dict)


def browse(request, region='any', category='any'):
    context_dict = {
        'regions': Region.objects.all(),
        'categories': Category.objects.all(),
        'tagSuggestions': list(Tag.objects.values_list('name', flat=True))
    }

    if region != 'any':
        context_dict['selected_region'] = region

    if category != 'any':
        context_dict['selected_category'] = category

    return render(request, 'places/browse.html', context_dict)


def api(request):
    query = Q()

    categories = json.loads(request.GET.get('categories', '[]'))
    if len(categories) > 0:
        query &= Q(category__slug__in=categories)

    regions = json.loads(request.GET.get('regions', '[]'))
    if len(regions) > 0:
        query &= Q(region__slug__in=regions)

    tags = json.loads(request.GET.get('tags', '[]'))
    tags = filter(None, tags)
    if len(tags) > 0:
        query &= Q(tags__name__in=tags)

    results = Place.objects.filter(query).distinct()

    places = [model_to_dict(result, fields=['name', 'title', 'subtitle']) for result in results]
    thumbnails = [get_thumbnail('covers/' + place.coverImage, '400x400', crop='center', quality=99).url for place in results]

    return HttpResponse(json.dumps({'places': places, 'thumbnails': thumbnails}))


def weather(request):
    return render(request, 'places/weather.html')


def details(request, slug):
    place_slug = slug
    place = Place.objects.get(slug=place_slug)
    experience = Experience.objects.all()
    media_directory = settings.MEDIA_ROOT

    images = []
    for filename in os.listdir(os.path.join(media_directory, 'gallerys', place_slug)):
        images.append('gallerys/' + place_slug + '/' + filename)

    context_dict = {
        'place': place,
        'gallery': images,
        'experiences': experience,
    }

    return render(request, 'places/details.html', context_dict)


class PlaceDetailView(SingleObjectMixin, ListView):
        model = Place
        template_name = 'places/index_place1.html'

        def get(self, request, *args, **kwargs):
            self.object = self.get_object(queryset=Place.objects.all())
            return super().get(request, *args, **kwargs)

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)

            place = get_object_or_404(Place, slug=self.kwargs.get('slug'))

            media_directory = settings.MEDIA_ROOT
            images = []
            for filename in os.listdir(os.path.join(media_directory, 'gallerys', place.slug)):
                images.append('gallerys/' + place.slug + '/' + filename)

            context['attractions'] = place.attraction_set.all()
            context['place'] = self.object
            context['gallerys'] = images
            context['experiences'] = Experience.objects.filter(location=place)
            context['posts'] = Post.objects.filter(location=place)
            context['regions'] = Region.objects.all()
            return context


class AttractionDetailView(SingleObjectMixin, ListView):
    model = Attraction
    template_name = 'places/index_attraction.html'

    def get(self, request, *args, **kwargs):
        self.object =self.get_object(queryset=Attraction.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        attraction = get_object_or_404(Attraction, slug=self.kwargs.get('slug'))
        places = attraction.place.all()
        media_directory = settings.MEDIA_ROOT
        images = []
        for filename in os.listdir(os.path.join(media_directory, 'gallerys', attraction.slug)):
            images.append('gallerys/' + attraction.slug + '/' + filename)

        context['attractions'] = Attraction.objects.filter(location__in=places).distinct()
        context['places'] = places
        context['attraction'] = self.object
        context['gallerys'] = images
        context['experiences'] = Experience.objects.filter(location__in=places).distinct()
        context['posts'] = Post.objects.filter(location__in=places).distinct()
        return context


class SearchView(TemplateView):
    template_name = 'places/index-city-2.html'
    model = Place

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        self.results = Post.objects.filter(name__icontains=q)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(results=self.results, **kwargs)



class HomeView(ListView):
    template_name = 'places/index.html'
    model = Place

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        types1 = Type.objects.all()

        context['attractions'] = Attraction.objects.all()
        context['experiences'] = Experience.objects.all()
        context['types'] = types1
        context['all'] = prefetch_related_objects(types1, 'place_set')
        context['trips'] = Trip.objects.all()
        context['regions'] = Region.objects.all()

        # [{'name': type.name, 'places': [{'name': place.name, 'pets':]} for child in parent.children.all()]} for parent in parents]

        return context

    #
    # def get(self, request, *args, **kwargs):
    #     self.object =self.get_object(queryset=Attraction.objects.all())
    #     return super().get(request, *args, **kwargs)
    #
    # def get_context_data(self, **kwargs):
    # context = super().get_context_data(**kwargs)
    #
    # context['attractions'] = Attraction.objects.all()
    # context['places'] = Place.objects.all()
    # context['experiences'] = Experience.objects.all()
    #     context['posts'] = Post.objects.all()
    #     context['categories'] = Category.objects.all()
    #     context['types'] = Type.objects.all().prefetch_related('place_set').all()

        # return context
