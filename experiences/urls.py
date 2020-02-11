from django.urls import path
from django.urls import path
from .views import ExperienceListView, ExperienceDetailView, CategoryDetailView, TripDetailView, TripSearchList, TripListView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', ExperienceListView.as_view(), name='experience-home'),
    path('<str:slug>/', ExperienceDetailView.as_view(), name='experience-details'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category-details'),
    path('trips/<str:slug>/', TripDetailView.as_view(), name='trip-details'),
    path('trip', TripListView.as_view(), name='trip-home'),
    path('trips/search/', TripSearchList.as_view(), name='trip-details'),

    # path('', PostList.as_view(), name='blog-home'),
    # path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    # path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
    # path('post/new/', PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # path('about/', views.about, name='blog-about'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
