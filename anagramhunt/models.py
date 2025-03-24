from django.db import models
from django.conf import settings
from django.urls import reverse
class Anagramhunt(models.Model):
    play = models.CharField(max_length=200)

    def __str__(self):
        return self.play
class PlayerScores(models.Model):
    wordgame = models.ForeignKey(Anagramhunt, on_delete=models.CASCADE)
    score = models.IntegerField
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.wordgame.name} - {self.score}"