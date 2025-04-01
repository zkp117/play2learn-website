from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import ContactApplicationForm

class ContactAppView(FormView):
    template_name = 'connect/contact_page.html'
    form_class = ContactApplicationForm
    success_url = reverse_lazy('contact:thanks')

class ContactAppThanksView(TemplateView):
    template_name = 'connect/thanks.html'