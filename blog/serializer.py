from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import CustomUser , Post


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'phone', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def validate_password(self, value):
        validate_password(value)
        return value

#Post serializer
class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
    def create(self, validated_data):
        request = self.context.get('request')
        if not request or not request.user or not request.user.is_authenticated:
            raise serializers.ValidationError({'error': 'invalid request user must be logged in'})
        validated_data['author'] = request.user
        return Post.objects.create(**validated_data)



