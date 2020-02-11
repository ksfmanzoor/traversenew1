from django.urls import path
from .views import HotelDetailView
from .import views


urlpatterns = [

     # path('browse/<str:region>/<str:category>/', views.browse, name='browse'),
     path('details/<str:slug>', HotelDetailView.as_view(), name='hotel-details'),
     # path('attractions/<str:slug>', AttractionDetailView.as_view(), name='attraction-details'),
     # path('', views.index, name='index'),
     # path('api/', views.api, name='api'),
     # path('weather/', views.weather, name='api'),
     # path('details/<str:slug>', views.details, name='details'),

]

