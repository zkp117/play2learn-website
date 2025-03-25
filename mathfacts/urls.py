from django.urls import path
from .views import MathGameView, MathScoreView

app_name = 'mathfacts'
urlpatterns = [
    path('mathfacts/<slug>/play/', MathGameView.as_view(), name='play'),
    path('mathfacts//<slug>/scores/', MathScoreView.as_view(), name='math_score_list')
]