from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from allauth.account.views import PasswordChangeView
from .forms import CustomUserChangeForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def user_account_view(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('my_account')
        else:
            form = CustomUserChangeForm(instance=request.user)

        return render(request, "account/my_account.html", {"form": form})
class CustomPasswordChangeView( SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('my_account')
class MyAccountPageView( SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    success_message = 'Update Successful'
    template_name = 'account/my_account.html'

    def get_object(self):
        return self.request.user
