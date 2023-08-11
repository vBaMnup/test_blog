from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Blog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, auto_created=True)

    def __str__(self):
        return f"блог пользователя {self.user}"


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
