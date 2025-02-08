from .models import Post, Comments, CustomUser
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

#User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'phone', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
    def validate_password(self, value):
        validate_password(value)
        return value





# class CommentSerializer(serializers.ModelSerializer):
#     author = serializers.StringRelatedField()
#     post = serializers.StringRelatedField()
#
#     class Meta:
#         model = Comments
#         fields = ['content', 'post', 'author']
#
#
# class PostSerializer(serializers.ModelSerializer):
#     author = serializers.StringRelatedField()
#     comments = CommentSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Post
#         fields = ['title', 'content', 'author', 'comments']
