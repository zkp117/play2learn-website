from django.db import models
class Mathfacts(models.Model):
    play = models.CharField(max_length=200)

    def __str__(self):
        return self.play