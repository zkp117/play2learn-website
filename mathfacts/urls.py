from django.urls import path
from .views import MathGameView, MathScoreView, MathScoreDetailView

app_name = 'mathfacts'
urlpatterns = [
    path('mathfacts/<int:pk>/play/', MathGameView.as_view(), name='play'),
    path('', MathScoreView.as_view(), name='list'),
    path('score/<int:pk>/', MathScoreDetailView.as_view(), name='math_score_detail'),
]