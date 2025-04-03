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

        content = f'''<p>Hey {first_name}</p>
        <p>Questions & feedback</p>
        <ol>'''

        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'

        content += '</ol>'

    # sends email to admin / sendgrid account owner (email I use is neeneez2008@gmail.com)
        send_email('neeneez2008@gmail.com', 'Questions & feedback', content)

    # sending the email to the user (to the email address they entered in the form)
        user_email = data.get('email')
        if user_email:
            send_email(
                user_email,
                'Your Questions & Feedback Received',
                '<p>Thank you for reaching out to us! We will respond in 3 - 5 business days</p>'
            )

        return super().form_valid(form)
class ContactAppThanksView(TemplateView):
    template_name = 'connect/thanks.html'