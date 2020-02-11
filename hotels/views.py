from django.shortcuts import render

from django.views.generic import DetailView, ListView
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import get_object_or_404
from hotels.models import Hotel
# Create your views here.


class HotelDetailView(SingleObjectMixin, ListView):
        model = Hotel
        template_name = 'hotels/index_hotel.html'

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

            context['attractions'] = place.attraction_set
            context['place'] = self.object
            context['gallerys'] = images
            context['experiences'] = Experience.objects.filter(location=place)
            context['posts'] = Post.objects.filter(location=place)
            return context