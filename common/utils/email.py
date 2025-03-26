import os
import sendgrid
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

def send_email(to, subject, content, sender="neeneez2008@gmail.com"):
    sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
    mail = Mail(
        from_email=sender,
        to_emails=to,
        subject=subject,
        html_content=content
    )
    print(f"DEBUG: Sending email from {sender} to {to}...") # extra confirmation that the email went through
    return sg.send(mail)
