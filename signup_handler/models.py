from django.conf import settings
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import Usermanager
from django.core import validators

class User(AbstractUser):
    mobile = models.CharField(max_length = 14, default = '')
    profile_pic = models.ImageField(upload_to = 'profile_photos/', default = '', validators = [validators.validate_image_file_extension])

    objects = Usermanager

    USERNAME_FIELD: 'AbstractUser.username'
    
    REQUIRED_FIELDS: list([])
