from .models import Post, Comments, CustomUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'phone', 'first_name', 'last_name']


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
