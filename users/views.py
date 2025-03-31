from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from allauth.account.views import PasswordChangeView
from .forms import CustomUserChangeForm
from django.contrib.messages.views import SuccessMessageMixin
class CustomPasswordChangeView( SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('my-account')
class MyAccountPageView( SuccessMessageMixin, LoginRequiredMixin, UpdateView):

    model = get_user_model()
    form_class = CustomUserChangeForm
    success_message = 'Update Successful'
    success_url = reverse_lazy('my-account')
    template_name = '/my-account.html'

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
            response = super().form_valid(form)
            print("Form Errors:", form.errors)  # Debugging
            return response
