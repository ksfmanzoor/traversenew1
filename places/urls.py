from django.urls import path
from .views import PlaceDetailView, AttractionDetailView
from experiences.views import ExperienceSearchView
from .import views


urlpatterns = [

     path('browse/<str:region>/<str:category>/', views.browse, name='browse'),
     path('details/<str:slug>', PlaceDetailView.as_view(), name='place-details'),
     path('attractions/<str:slug>', AttractionDetailView.as_view(), name='attraction-details'),
     path('search/', ExperienceSearchView.as_view(), name='experience-search'),
     path('', views.index, name='index'),
     path('api/', views.api, name='api'),
     path('weather/', views.weather, name='api'),
     # path('details/<str:slug>', views.details, name='details'),

]