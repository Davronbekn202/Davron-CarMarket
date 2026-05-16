from django.core.mail import send_mail
from django.conf import settings

def send_reset_password_email(email, code):
    send_mail(
        subject="Password Reset OTP",
        message=f"Your OTP code is: {code}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )