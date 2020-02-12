# Create your views here.
import os
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from experiences.models import Experience, Category, Trip
from django.conf import settings
from django.shortcuts import get_object_or_404, get_list_or_404
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from places.models import Place, Region
from .models import Booking, TripBooking, ExperienceBooking
from .forms import TripBookingCreateForm

class BookingManager(ListView):
    model = Booking
    template_name = 'bookings/booking_manager.html'

    def get(self, request, *args, **kwargs):
        self.object = Booking.objects.all()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        user_name = self.request.GET['user']
        
        # Add in the category
        context['category_list'] = Category.objects.all()
        context['trips'] = Trip.objects.all()
        return context


class TripBookingCreateView(ListView):
    template_name = 'experiences/book_now.html'
    form_class = TripBookingCreateForm
    

class TripBookingView(SingleObjectMixin, ListView):
    model = TripBooking
    template_name = 'bookings/book_now.html'
    context_object_name = 'experience'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Experience.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        TripBooking.booked_trip = self.request.GET['trip']
        context['experiences'] = Experience.objects.filter(location__region__slug=region_name)
        context['trips'] = Trip.objects.filter(location__region__slug=region_name)
        context['selected_region'] = Region.objects.filter(slug=region_name)
        context['regions'] = Region.objects.all()
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


