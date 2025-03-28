from allauth.account.models import EmailConfirmation
from django.shortcuts import render

def send_confirmation(request, user):
    confirmation = EmailConfirmation.objects.filter(user=user).first()
    context = {'confirmation': confirmation}
    return render(request, 'account/email_confirm.html', context)
