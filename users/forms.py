from datetime import datetime
from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser


BIRTH_YEAR_CHOICES = range(1915, datetime.now().year)

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'dob')