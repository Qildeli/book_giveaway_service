from rest_framework import serializers
from django.contrib.auth import get_user_model


# Serializer for user registration
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # Custom or default user model defined in Django settings
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,  # Password shouldn't be readable in the response
                'min_length': 5  # Password length is at least 5 characters
            }
        }

    def create(self, validated_data):
        # Use create_user to ensure the password is hashed
        return get_user_model().objects.create_user(**validated_data)


# Serializer for user authentication
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
