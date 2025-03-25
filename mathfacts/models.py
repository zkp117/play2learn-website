from django.db import models
from django.conf import settings
from common.utils.text import unique_slug

MATH_OPERATIONS = [
    ('1', 'Addition'),
    ('2', 'Subtraction'),
    ('3', 'Multiplication'),
    ('4', 'Division'),
]
class Mathfacts(models.Model):
    play = models.CharField(max_length=100)

    def __str__(self):
        return self.play
class MathScore(models.Model):
    chosen_operation = models.CharField(
        max_length=1,
        choices = MATH_OPERATIONS,
        default = '1',
    )
    chosen_highest_number = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
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
        return f"{self.user.username} - Score: {self.score} - Level: {self.chosen_highest_number}"
    

