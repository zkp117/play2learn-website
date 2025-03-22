from django.urls import path
from .views import MathGameView, MathScoreView

app_name = 'mathfacts'
urlpatterns = [
    path('mathfacts/<int:pk>/play/', MathGameView.as_view(), name='play'),
    path('mathfacts/scores/', MathScoreView.as_view(), name='math_score_list')
]