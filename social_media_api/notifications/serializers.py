from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source='actor.username', read_only=True)
    # Expose the ID of the target object, as the full object is typically not serialized here
    target_object_id = serializers.CharField(source='object_id', read_only=True)

    class Meta:
        model = Notification
        # 'created_at' fulfills the 'timestamp' requirement
        fields = ('id', 'actor_username', 'verb', 'target_object_id', 'is_read', 'created_at')
        read_only_fields = ('id', 'actor_username', 'verb', 'target_object_id', 'is_read', 'created_at')
