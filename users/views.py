from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import CustomUserChangeForm

class MyAccountView(TemplateView):
    template_name = "account/my_account.html"

    def get(self, request, *args, **kwargs):
        form = CustomUserChangeForm(instance = request.user)
        return self.render_to_response({'form': form})
    
    def post(self, request, *args, **kwargs):
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('my-account')
        return self.render_to_response({'form': form})