from django.contrib import admin
from .models import WordScore

@admin.register(WordScore)
class WordScoreAdmin(admin.ModelAdmin):
    model = WordScore
    list_display = ['user', 'score', 'created', 'updated'
                    'wordlength']
    
    def updatedwordlength(self, obj):
        return len(obj.wordgame)  # Return the length of the 'wordgame' field
    updatedwordlength.admin_order_field = 'wordgame'  # Allow sorting by the wordgame field
    updatedwordlength.short_description = 'Word Game Length'  # Set a custom column header


    def get_readonly_fields(self, request, obj=None):
        if obj: 
            return ('created', 'updated')
        return ()
