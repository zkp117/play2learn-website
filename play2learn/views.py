from django.views.generic import TemplateView
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render
from django.shortcuts import redirect
class MyAccountView(TemplateView):
    template_name = "account/my_account.html" 

    def get(self, request, *args, **kwargs):
        form = UserChangeForm(instance = request.user)
        return self.render_to_response({'form': form})
    
    def post(self, request, *args, **kwargs):
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('my-account')
        
        return self.render_to_response({'form': form})

def my_play2learn(request):
    return render(request, 'myapp/my_play2learn.html')
