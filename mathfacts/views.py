from django.views.generic import ListView, TemplateView
from django.shortcuts import render
from .models import Mathfacts, MathScore

class MathGameView(TemplateView):
    def get(self, request, *args, **kwargs):
        mathgame = Mathfacts.objects.get(pk=kwargs['pk'])
        return render(request, 'mathfacts/play.html', {'mathgame': mathgame})

class MathScoreView(ListView):
    model = MathScore
    template_name = 'pages/math_scorelist.html'
    scores_list = 'math_scores'

    def get_queryset(self):
        return MathScore.objects.filter(mathgame_id=self.kwargs['mathgame_id']).order_by('-score')[:10]
    

class MathfactsCreateView(CreateView):
    model = Mathfacts
    form_class = MathForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)