from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.views import PasswordChangeView as DjangoPasswordChangeView
from .forms import CustomUserChangeForm
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

class CustomPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, DjangoPasswordChangeView):  # Renamed
    success_url = reverse_lazy('my-account')
class MyAccountPageView( SuccessMessageMixin, LoginRequiredMixin, UpdateView):

    model = get_user_model()
    form_class = CustomUserChangeForm
    success_message = 'Update Successful'
    success_url = reverse_lazy('my-account')
    template_name = 'account/my_account.html'

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
            response = super().form_valid(form)
            self.request.user.refresh_from_db()
            cache.clear()
            return response
    
@login_required
def clear_avatar(request):
    user = request.user
    user.avatar.delete()  # Delete the avatar file
    user.save()  # Save the user instance
    return redirect('my-account')  # Redirect back to the profile page
    