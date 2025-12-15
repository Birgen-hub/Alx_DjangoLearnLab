from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from django.shortcuts import get_object_or_404
from .models import User as CustomUser
from .serializers import AuthTokenSerializer, CustomUserSerializer, RegisterSerializer

# --- Authentication Views ---

class RegisterUserView(generics.CreateAPIView):
    """
    Create a new user in the system.
    """
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

class LoginUserView(ObtainAuthToken):
    """
    Create an authentication token for a user.
    """
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    permission_classes = (permissions.AllowAny,)

class ManageUserView(generics.RetrieveUpdateAPIView):
    """
    Manage the authenticated user's profile.
    """
    serializer_class = CustomUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """
        Retrieve and return the authenticated user.
        """
        return self.request.user

# --- Social Interaction Views ---

class FollowUserView(generics.GenericAPIView):
    """
    Allows the authenticated user to follow another user.
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CustomUser.objects.all()

    def post(self, request, pk):
        """
        Follow the user specified by the primary key (pk).
        """
        user_to_follow = get_object_or_404(CustomUser, pk=pk)
        
        if request.user == user_to_follow:
            return Response(
                {'detail': 'You cannot follow yourself.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if user_to_follow in request.user.following.all():
            return Response(
                {'detail': f'You are already following {user_to_follow.username}.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        request.user.following.add(user_to_follow)
        
        return Response(
            {'detail': f'Successfully followed {user_to_follow.username}.'},
            status=status.HTTP_200_OK
        )


class UnfollowUserView(generics.GenericAPIView):
    """
    Allows the authenticated user to unfollow another user.
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CustomUser.objects.all()

    def post(self, request, pk):
        """
        Unfollow the user specified by the primary key (pk).
        """
        user_to_unfollow = get_object_or_404(CustomUser, pk=pk)
        
        if request.user == user_to_unfollow:
            return Response(
                {'detail': 'You cannot unfollow yourself.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if user_to_unfollow not in request.user.following.all():
            return Response(
                {'detail': f'You are not following {user_to_unfollow.username}.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.user.following.remove(user_to_unfollow)

        return Response(
            {'detail': f'Successfully unfollowed {user_to_unfollow.username}.'},
            status=status.HTTP_200_OK
        )
