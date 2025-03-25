from django.db import models
from django.conf import settings
from common.utils.text import unique_slug

WORD_LENGTH = [
    ('5', '5 letters'),
    ('6', '6 letters'),
    ('7', '7 letters'),
    ('8', '8 letters'),
    ]
class Anagramhunt(models.Model):
    play = models.CharField(max_length=100)

    def __str__(self):
        return self.play
class WordScore(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField(default = 0)
    word_length = models.CharField(
        max_length = 1,
        choices = WORD_LENGTH,
        default = '5',
    )
    slug = models.SlugField(
        max_length=50, unique=True, null=True, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)  

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - Word Score: {self.score} - Length: {self.get_word_length_display()}"