from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

from datetime import date


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )

        return self._create_user(email, password, **extra_fields)


SALUTATION_CHOICES = (
    ('MALE', 'Herr'),
    ('FEMALE', 'Frau'),
    ('UNKNOWN', 'Unbekannt'),

)


# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, primary_key=True, verbose_name='E-Mail')
    salutation = models.CharField(max_length=15, choices=SALUTATION_CHOICES, default='Unbekannt', verbose_name='Anrede')
    birthday = models.DateField(default=date.today, verbose_name='Geburtstag')

    USERNAME_FIELD = "email"  # make the user log in with the email
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    objects = CustomUserManager()
