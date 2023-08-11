from django.urls import include, path


urlpatterns = [
    path("", include("src.blog.urls")),
    path("", include("src.users.urls")),
]
