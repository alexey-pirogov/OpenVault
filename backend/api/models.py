import os
from django.conf import settings
from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

from django.utils.translation import gettext_lazy as _


class Profile(AbstractUser):
    pass
