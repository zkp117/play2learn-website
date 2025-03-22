from django.views.generic import ListView
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

    def get_queryset(self):
        return Score.objects.filter(mathgame_id=self.kwargs['mathgame_id']).order_by('-score')[:10]