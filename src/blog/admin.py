from django.contrib import admin

from src.blog.models import Post, Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
