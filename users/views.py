from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from allauth.account.views import PasswordChangeView

from .forms import CustomUserChangeForm
from django.contrib.messages.views import SuccessMessageMixin
class CustomPasswordChangeView( SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('my_account')

class MyAccountPageView( SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    success_message = 'Update Successful'
    template_name = 'account/my_account.html'

    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("Context Data:", context)
        return context
