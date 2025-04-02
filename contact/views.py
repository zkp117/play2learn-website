import html
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from common.utils.email_service import send_email
from .forms import ContactStaffForm

class ContactAppView(FormView):
    template_name = 'connect/contact_us.html'
    form_class = ContactStaffForm
    success_url = reverse_lazy('contact:thanks')

    def form_valid(self, form):
        first_name = form.cleaned_data.get('first_name')
        data = form.cleaned_data
        to = 'neeneez2008@gmail.com'
        subject = 'Feedback for Play2Learn'
        content = f'''<p>Hey {first_name}!</p>
            <p>We have received your questions and feedback.
            We will get back to you in 3 - 5 business days.</p>
            <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        
        content += '</ol>'

        send_email(to, subject, content)
        return super().form_valid(form)

class ContactAppThanksView(TemplateView):
    template_name = 'connect/thanks.html'