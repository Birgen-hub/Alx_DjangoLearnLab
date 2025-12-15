from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Notification(models.Model):
    # Mandatory Fields
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='notifications'
    )
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='actions'
    )
    verb = models.CharField(max_length=255) # e.g., 'liked', 'followed', 'commented'
    
    # Target (GenericForeignKey)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    target = GenericForeignKey('content_type', 'object_id')
    
    # Timestamp (using created_at as timestamp)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        # The created_at field fulfills the 'timestamp' requirement

    def __str__(self):
        # target will resolve to the string representation of the related object (Post, Comment, etc.)
        return f"{self.actor.username} {self.verb} {self.target} (to {self.recipient.username})"
