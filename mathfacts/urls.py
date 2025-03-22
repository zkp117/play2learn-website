from django.urls import path
from .views import MathGameView

app_name = 'mathfacts'
urlpatterns = [
    path('mathfacts/<int:pk>/play/', MathGameView.as_view(), name='play'),
]