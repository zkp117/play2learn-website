from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from .models import Mathfacts, Score

class MathGameView(TemplateView):
    def get(self, request, *args, **kwargs):
        mathgame = Mathfacts.objects.get(pk=kwargs['pk'])
        return render(request, 'mathfacts/play.html', {'mathgame': mathgame})

class MathScoreView(ListView):
    model = Score
    template_name = 'mathfacts_scorelist.html'
    scores_list = 'math_scores'

class MathScoreDetailView(DetailView):
    model = Score
    template_name = 'mathfacts/score_detail.html'
    current_user_score = 'score'