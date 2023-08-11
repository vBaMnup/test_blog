from rest_framework.viewsets import ModelViewSet

from src.blog.models import Blog, Post
from src.blog.serializers import BlogSerializer, PostSerializer


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
