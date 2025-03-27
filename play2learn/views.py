from django.views.generic import TemplateView
from django.shortcuts import render

class MyAccountView(TemplateView):
    template_name = "account/my_account.html" 

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

def my_play2learn(request):
    return render(request, 'myapp/my_play2learn.html')
