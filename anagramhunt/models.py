from django.db import models
from django.contrib.auth.models import User
class Anagramhunt(models.Model):
    play = models.CharField(max_length=200)

    def __str__(self):
        return self.play
class WordScore(models.Model):
    wordgame = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
        return f"{self.user.username} - Word Score: {self.score}"