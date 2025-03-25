from django.db import models
from django.conf import settings

WORD_LENGTHS = [
        ('5', '5 length'),
        ('6', '6 length'),
        ('7', '7 length'),
        ('8', '8 length'),
    ]
class Anagramhunt(models.Model):
    play = models.CharField(max_length=200)

    def __str__(self):
        return self.play
class WordScore(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField(default = 0)
    wordlengths = models.CharField(
        max_length = 1,
        choices = WORD_LENGTHS,
        default = '5',
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)  

    def __str__(self):
        # Use get_wordlength_display() to return the human-readable choice value
        return f"{self.user.username} - Word Score: {self.score} - Length: {self.get_wordlengths_display()}"