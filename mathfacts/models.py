from django.db import models
from django.conf import settings
class Mathfacts(models.Model):
    play = models.CharField(max_length=200)

    def __str__(self):
        return self.play
class MathScore(models.Model):
    mathgame = models.ForeignKey(Mathfacts, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField
    created = models.DateTimeField(auto_now_add=True)  # Add this
    updated = models.DateTimeField(auto_now=True)  # Add this

    def __str__(self):
        return f"{self.user.username} - Word Score: {self.score}"
    

