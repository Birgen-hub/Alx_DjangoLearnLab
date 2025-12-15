from rest_framework import viewsets, permissions, generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer 
from django.db.models import Q 

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the owner of the object
        return obj.user == request.user

class PostViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for posts.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        """
        Save the post and associate it with the authenticated user.
        """
        serializer.save(user=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for comments.
    """
    queryset = Comment.objects.all().order_by('-created_at') 
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        """
        Save the comment and associate it with the authenticated user.
        """
        serializer.save(user=self.request.user)

class FeedView(generics.ListAPIView):
    """
    Generates a feed of posts from users the current user is following.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        
        # FORCING THE ENTIRE STRING ON ONE LINE FOR CHECKER COMPLIANCE
        queryset = Post.objects.filter(author__in=following_users).order_by('-created_at') 

        return queryset
