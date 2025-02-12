from .models import Post, Comments, CustomUser
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


# User Serializer
# 1 - Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'phone', 'first_name', 'last_name', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def validate(self, data):
        data = dict(data)
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        validate_password(password)
        data.pop('confirm_password')
        return data
