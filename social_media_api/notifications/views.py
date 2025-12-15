from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return notifications only for the currently authenticated user, ordered by created_at (timestamp)
        return Notification.objects.filter(recipient=self.request.user).order_by('-created_at')

class NotificationMarkAsReadView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Only allow marking notifications that belong to the user and are unread
        return Notification.objects.filter(recipient=self.request.user, is_read=False)

    def perform_update(self, serializer):
        # Force the update to set is_read to True
        serializer.instance.is_read = True
        serializer.save()
        
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_update(self.get_serializer(instance))
        return Response(NotificationSerializer(instance).data, status=status.HTTP_200_OK)
