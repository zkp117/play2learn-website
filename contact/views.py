from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import ContactStaffForm

class ContactAppView(FormView):
    template_name = 'connect/contact-page.html'
    form_class = ContactStaffForm
    success_url = reverse_lazy('jobs:thanks')

class ContactAppThanksView(TemplateView):
    template_name = 'connect/thanks.html'