from django.views.generic import TemplateView
from django.shortcuts import render

class MyAccountView(TemplateView):
    template_name = "my_account.html" 

def my_account(request):
    # Your logic here, return the correct template
    return render(request, 'myapp/my_account.html')

def my_play2learn(request):
    # Your logic here, return the correct template
    return render(request, 'myapp/my_play2learn.html')
