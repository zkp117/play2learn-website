from django.db import models
from django.conf import settings
class Mathfacts(models.Model):
    play = models.CharField(max_length=100)

    def __str__(self):
        return self.play
class MathScore(models.Model):
    mathgame = models.ForeignKey(Mathfacts, on_delete=models.CASCADE)
    highest_number = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Score: {self.score} - Level: {self.highest_number}"
    

