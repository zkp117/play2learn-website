from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from .models import Mathfacts

class MathGameView(TemplateView):
    def get(self, request, *args, **kwargs):
        mathgame = Mathfacts.objects.get(pk=kwargs['pk'])
        return render(request, 'mathfacts/play.html', {'mathgame': mathgame})

class MathScoreView(ListView):
    model = Score

class MathScoreDetailView(DetailView):
    model = Score