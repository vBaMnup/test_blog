from django.contrib.auth import get_user_model
from rest_framework import serializers

from src.blog.models import Blog, Post

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class PostInBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "text")


class BlogSerializer(serializers.ModelSerializer):
    posts = PostInBlogSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ("id", "user", "posts")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "text", "blog")
