from django.urls import path
from .views import (
    RegisterUserView,
    LoginUserView,
    ManageUserView,
    FollowUserView,
    UnfollowUserView
)

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('me/', ManageUserView.as_view(), name='me'),
    
    # Social Interaction URLs
    path('<int:pk>/follow/', FollowUserView.as_view(), name='follow-user'),
    path('<int:pk>/unfollow/', UnfollowUserView.as_view(), name='unfollow-user'),
]
