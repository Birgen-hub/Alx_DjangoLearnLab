from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.authtoken.models import Token # Added Token import

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model. Used for retrieving and updating user details.
    """
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'bio', 'profile_picture')
        read_only_fields = ('id', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        """
        Create a new user with encrypted password using create_user.
        """
        user = get_user_model().objects.create_user(**validated_data)
        return user

class AuthTokenSerializer(serializers.Serializer):
    """
    Serializer for the user authentication token.
    Handles login using email and password.
    """
    email = serializers.EmailField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """
        Validate and authenticate the user.
        """
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(
                request=self.context.get('request'),
                username=email,
                password=password
            )
            
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
