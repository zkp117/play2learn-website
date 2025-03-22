from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Mathfacts

class MathGameView(TemplateView):
    def get(self, request, *args, **kwargs):
        mathgame = Mathfacts.objects.get(pk=kwargs['pk'])
        return render(request, 'mathfacts/play.html', {'mathgame': mathgame})
