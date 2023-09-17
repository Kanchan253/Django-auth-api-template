from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

class Util:

    def verify_mail(email, token, user_id, username):
        link = settings.URL+"auth"
        html_tpl_path = render_to_string('emailverify.html', {
            'link': link, 'username': username, 'user_id': user_id, 'token': token})
        subject = 'Verify your email'
        message = "Thank you for visiting"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from,
                  recipient_list, html_message=html_tpl_path)
        return True
