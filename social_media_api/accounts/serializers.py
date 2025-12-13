from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'following', 'followers']
        read_only_fields = ['followers']
