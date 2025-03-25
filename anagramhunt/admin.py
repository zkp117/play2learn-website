from django.contrib import admin
from .models import WordScore

@admin.register(WordScore)
class WordScoreAdmin(admin.ModelAdmin):
    model = WordScore
    list_display = ['user', 'score', 'created', 'updated',
                    'word_lengths']
    
    def get_word_length_display(self, obj):
        return obj.get_wordlengths_display()
    get_word_length_display.short_description = 'Word Length'
    
    def get_readonly_fields(self, request, obj=None):
        if obj: 
            return ('created', 'updated')
        return ()
