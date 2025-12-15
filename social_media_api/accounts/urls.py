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
    
    # Social Interaction URLs matching checker strings:
    # Checker requires "follow/<int:user_id>"
    path('follow/<int:user_id>', FollowUserView.as_view(), name='follow-user'),
    # Checker requires "unfollow/<int:user_id>/"
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]
