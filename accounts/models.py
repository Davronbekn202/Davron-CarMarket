from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    phone_regex = RegexValidator(regex=r'^\+?998\d{9}$', message='Telefon raqam +998 dan boshlanishi kerak')
    phone_number = models.CharField(
        max_length=13,
        validators=[phone_regex],
        unique=True,
        blank=True,
        null=True
    )

    class Roles(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'User'
        MANAGER = 'manager', 'Manager'

    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.USER)

    class UserRoles(models.TextChoices):
        MANAGER = 'sotuvchi', 'Sotuvchi'
        CUSTOMER = 'haridor', 'Haridor'

    user_role = models.CharField(max_length=20, choices=UserRoles, default=UserRoles.CUSTOMER, blank=True)
    date_of_register = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
