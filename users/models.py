from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.contrib import admin
from allauth.socialaccount.models import SocialApp
from django.contrib.admin.sites import NotRegistered

# Only unregister SocialApp if it's already registered
try:
    admin.site.unregister(SocialApp)
except NotRegistered:
    pass  # SocialApp is not registered, so just ignore it


def validate_avatar(value):
    w, h = get_image_dimensions(value)
    if w > 200 or h > 200:
        raise ValidationError('Avatar must be no bigger than 200x200 pixels.')
class CustomUser(AbstractUser):
    dob = models.DateField(
        verbose_name="Date of Birth", null=True, blank=True
    )
    avatar = models.ImageField(upload_to='avatars/', blank=True,
    help_text='Image must be 200px by 200px.',
    validators=[validate_avatar]
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.username})'

    def get_absolute_url(self):
        return reverse('my-account')