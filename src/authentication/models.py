from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    email = models.EmailField(blank=False, null=False)
    first_name = models.CharField(_("first name"), max_length=150, blank=False, null=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False, null=False)
    phone_number = models.CharField(_("phone number"), max_length=20, null=True)
    photo = models.ImageField(default='resources/images/default_user_photo.jpg')
    is_premium_user = models.BooleanField(_("is premium user"), default=False)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
