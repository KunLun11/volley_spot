from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from base.models.bases import BaseModelIDTime


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

    def create_organizer(self, email, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_organizer", True)
        extra_fields.setdefault("is_staff", True)
        return self.create_user(email, password, phone, **extra_fields)


class User(BaseModelIDTime, AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    objects = UserManager()

    email = models.EmailField("Email", unique=True, blank=True)
    phone = PhoneNumberField("Номер телефона", unique=True, blank=True)
    email_activated = models.BooleanField("Почта активирована", default=False, blank=True)
    phone_activated = models.BooleanField("Номер телефона активирован", default=False, blank=True)
    is_active = models.BooleanField("Активный", default=True)
    is_staff = models.BooleanField("Является администратором", default=False)
    is_organizer = models.BooleanField("Является организатором", default=False)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"*{self.pk} {self.email}"


__all__ = [
    "User",
]
