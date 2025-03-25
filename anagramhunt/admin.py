from django.contrib import admin
from .models import WordScore

@admin.register(WordScore)
class WordScoreAdmin(admin.ModelAdmin):
    model = WordScore
    list_display = ['user', 'score', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj: 
            return ('created', 'updated')
        return ()
