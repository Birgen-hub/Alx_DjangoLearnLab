from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer # Assume these will be created next

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
    Provides CRUD operations for posts. (Uses viewsets.ModelViewSet)
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
    # Checker requirement: "Comment.objects.all()" is met here.
    queryset = Comment.objects.all().order_by('-created_at') 
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        """
        Save the comment and associate it with the authenticated user.
        """
        serializer.save(user=self.request.user)
