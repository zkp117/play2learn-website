import sendgrid
from sendgrid.helpers.mail import Mail
from django.conf import settings

def send_email(to, subject, content):
    try:
        sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
        email = Mail(
            from_email="neeneez2008@gmail.com",  # Use a valid email address
            to_emails=to,
            subject=subject,
            html_content=content
        )
        response = sg.send(email)
        print(f"Email sent! Status: {response.status_code}, Response body: {response.body}")
        return response.status_code
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return None
