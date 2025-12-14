from django.urls import path
from .views import RegisterView, LoginView, UserProfileView, FollowUserView, UnfollowUserView, UserListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    
    path('users/', UserListView.as_view(), name='user_list'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    
    path('follow/<int:pk>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:pk>/', UnfollowUserView.as_view(), name='unfollow_user'),
]
