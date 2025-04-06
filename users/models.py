from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from play2learn.storage_backends import PublicMediaStorage  # Make sure this is imported correctly

def validate_avatar(value):
    w, h = get_image_dimensions(value)
    if w > 500 or h > 500:
        raise ValidationError('Avatar must be no bigger than 500x500 pixels.')

class CustomUser(AbstractUser):
    dob = models.DateField(
        verbose_name="Date of Birth", null=True, blank=True
    )
    avatar = models.ImageField(upload_to='avatars/', 
    storage=PublicMediaStorage(), 
    blank=True, 
    null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.username})'

    def get_absolute_url(self):
        return reverse('my-account')
