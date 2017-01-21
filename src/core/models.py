from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """A custom user model"""

    email = models.EmailField(verbose_name=_('Email'), unique=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']
