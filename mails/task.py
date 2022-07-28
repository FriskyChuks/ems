from celery import shared_task
from django.core.mail import send_mail

from accounts.models import User
from ems import settings

@shared_task(bind=True)
def send_mail_func(self):
    users = User.objects.all()
    for user in users:
        mail_subject = 'Hi! EMS testing Celery'
        message = 'I hope this message finds you well. From EMS@CIL'
        to_email = user.email
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=False,
        )
    return 'Done Sending mail'