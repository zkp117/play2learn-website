from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Anagramhunt 

class AnagramGameView(TemplateView):
    def get(self, request, *args, **kwargs):
        wordgame = Anagramhunt.objects.get(pk=kwargs['pk'])
        return render(request, 'anagramhunt/play.html', {'wordgame': wordgame})
