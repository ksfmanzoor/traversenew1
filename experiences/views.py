import os
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from .models import Experience, Category, Trip
from django.conf import settings
from django.shortcuts import get_object_or_404, get_list_or_404
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from places.models import Place, Region


class ExperienceListView(ListView):
    model = Experience
    template_name = 'experiences/exp_home.html'


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the category
        context['category_list'] = Category.objects.all()
        context['experiences'] = Experience.objects.all()
        context['regions'] = Region.objects.all()

        return context


class ExperienceSearchView(ListView):
    template_name = 'experiences/exp_results.html'
    model = Experience

    def get(self, request, *args, **kwargs):
        self.object = Experience.objects.all()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        region_name = self.request.GET['region']
        context['trips'] = Trip.objects.filter(location__region__slug=region_name).distinct()
        context['selected_region'] = Region.objects.filter(slug=region_name)
        context['regions'] = Region.objects.all()
        return context


class ExperienceDetailView(SingleObjectMixin, ListView):
    model = Experience
    template_name = 'experiences/exp_page.html'
    context_object_name = 'experience'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Experience.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        categories= self.object.category.all()
        context = super().get_context_data(**kwargs)
        experience = get_object_or_404(Experience, slug=self.kwargs.get('slug'))
        media_directory = settings.MEDIA_ROOT
        images = []
        for filename in os.listdir(os.path.join(media_directory, 'gallerys', experience.slug)):
            images.append('gallerys/' + experience.slug + '/' + filename)

        context['gallerys'] = images
        context['experience'] = self.object
        context['places'] = self.object.location.all()
        context['experiences'] = Experience.objects.filter(category__in=categories)
        return context


class TripDetailView(SingleObjectMixin, ListView):
    model = Trip
    template_name = 'experiences/trip_page.html'
    context_object_name = 'experience'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Trip.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        categories= self.object.category.all()
        context = super().get_context_data(**kwargs)
        trip = get_object_or_404(Trip, slug=self.kwargs.get('slug'))
        media_directory = settings.MEDIA_ROOT
        images = []
        for filename in os.listdir(os.path.join(media_directory, 'gallerys', trip.slug)):
            images.append('gallerys/' + trip.slug + '/' + filename)

        context['gallerys'] = images
        context['trip'] = self.object
        context['experiences'] = self.object.experiences.all()
        context['places'] = self.object.location.all()
        context['attractions'] = self.object.attractions.all()
        context['trips'] = Trip.objects.all()
        return context


class TripListView(ListView):
    model = Trip
    template_name = 'experiences/trip_home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the category
        context['regions'] = Region.objects.all()
        context['category_list'] = Category.objects.all()
        context['trips'] = Trip.objects.all()
        return context


class CategoryDetailView(SingleObjectMixin, ListView):
    model = Category
    template_name = 'experiences/cat_exp_page.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Category.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        context['category'] = self.object
        context['experiences'] = Experience.objects.filter(category=category_slug )
        return context

    # def get_queryset(self):
    #     category_id = get_object_or_404(Category, pk=self.kwargs.get('pk'))
    #     return Experience.objects.filter(category=category_id)


class ExperienceCreateView(CreateView):
    model = Experience
    template_name = 'experiences/experience-create.html'
    fields = ['title', 'name', 'content', 'image', 'date_posted']

    def get_queryset(self):
        categories = get_list_or_404(Category, name=self.kwargs.get('title'))
        return Experience.objects.filter(Category=categories)


class TripFilter(BaseFilter):
    search_fields = {
        'search_text' : ['location', 'attractions'],
        'search_price_exact' : { 'operator' : '__exact', 'fields' : ['price'] },
        'search_price_min' : { 'operator' : '__gte', 'fields' : ['price'] },
        'search_price_max' : { 'operator' : '__lte', 'fields' : ['price'] },
    }


class TripSearchList(SearchListView):
  # regular django.views.generic.list.ListView configuration
  model = Trip
  template_name = "experiences/exp_results.html"

  # additional configuration for SearchListView
  filter_class = TripFilter