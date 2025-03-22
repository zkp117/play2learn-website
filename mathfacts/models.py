from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
class Mathfacts(models.Model):
    play = models.CharField(max_length=200)

    def __str__(self):
        return self.play
    
class PlayerScores(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mathgame = models.ForeignKey(Mathfacts, on_delete=models.CASCADE)
    score = models.IntegerField
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.mathgame.name} - {self.score}"