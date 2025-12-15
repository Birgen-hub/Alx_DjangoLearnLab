from django.urls import path
from .views import PostListCreateView, PostDetailView, UserFeedView, LikePostView, UnlikePostView

urlpatterns = [
    path('feed/', UserFeedView.as_view(), name='user_feed'),
    
    path('posts/', PostListCreateView.as_view(), name='post_list_create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike_post'),
]
