from django.urls import include, path
from rest_framework import routers

from src.blog.views import BlogViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r"blog", BlogViewSet)
router.register(r"post", PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
