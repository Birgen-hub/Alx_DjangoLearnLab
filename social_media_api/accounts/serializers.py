from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()


    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'bio')

    def create(self, validated_data):
        # Create user
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            bio=validated_data.get('bio', '')
        )
        # Create token
        Token.objects.create(user=user)
        return user

class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'bio', 'followers_count')

