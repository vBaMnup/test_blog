from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver

from src.blog.models import Blog


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @receiver(models.signals.post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Blog.objects.create(user=instance)

    @receiver(models.signals.post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
