from django.urls import path
from .views import PostListView, PostList, PostDetail, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-details'),
    # path('', PostList.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    # path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),

]


urlpatterns = format_suffix_patterns(urlpatterns)
