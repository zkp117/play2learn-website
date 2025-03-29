from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .forms import CustomUserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

class MyAccountPageView(TemplateView):
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
    
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'account/change_password.html'
    success_url = reverse_lazy('my_account')
