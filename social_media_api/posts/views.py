from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from .models import Post, Like
from .serializers import PostSerializer, PostCreateSerializer
from accounts.models import User
from notifications.models import Notification

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostCreateSerializer
        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.user.following.all()
        
        queryset = Post.objects.filter(user__in=following_users).order_by('-created_at')
        
        return queryset

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        
        # Prevent user from liking their own post
        if post.user == request.user:
            return Response({"detail": "You cannot like your own post."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check and create the Like object
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if created:
            # Create a notification for the post owner
            content_type = ContentType.objects.get_for_model(Post)
            
            Notification.objects.create(
                recipient=post.user,
                actor=request.user,
                verb='liked',
                content_type=content_type,
                object_id=post.pk
            )
            
            return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "Post already liked."}, status=status.HTTP_200_OK)

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            # No notification generated for unliking
            return Response({"detail": "Post unliked successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_404_NOT_FOUND)
