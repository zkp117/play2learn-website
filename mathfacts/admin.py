from django.contrib import admin

from .models import MathScore

@admin.register(MathScore)
class MathScoreAdmin(admin.ModelAdmin):
    model = MathScore
    list_display = ['user', 'score', 'created', 'updated',
                    'highest_number', 'chosen_operation']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created', 'updated')

        return ()