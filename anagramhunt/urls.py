from django.urls import path
from .views import AnagramGameView

app_name = 'anagramhunt'
urlpatterns = [
    path('anagramhunt/<slug>/play/', AnagramGameView.as_view(), name='play'),
]