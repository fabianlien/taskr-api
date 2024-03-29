from django.db import models
from .validators import validate_file_size
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=300, blank=True)
    profile_image = models.ImageField(
        upload_to='images/',
        default='../default_profile_x3wzpb',
        validators=[validate_file_size]
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


models.signals.post_save.connect(create_profile, sender=User)
