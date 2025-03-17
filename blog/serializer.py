from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import CustomUser


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'phone', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def validate_password(self, value):
        validate_password(value)
        return value
