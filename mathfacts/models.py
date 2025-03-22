from django.db import models
from django.conf import settings
class Mathfacts(models.Model):
    play = models.CharField(max_length=200)

    def __str__(self):
        return self.play
class PlayerScore(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )
    created = models.DateTimeField(auto_now_add=True)