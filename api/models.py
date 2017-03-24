from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from hashid_field import HashidField

from accounts.mixins import TimestampMixin
from core.utils import timestamp_seconds


class ApiToken(TimestampMixin):

    token = HashidField(
        min_length=32,
        alphabet='0123456789abcdef',
        default=timestamp_seconds,
        unique=True,
        editable=True
    )
    owner = models.OneToOneField(User, related_name="token")

    def __str__(self):
        return self.token.hashid
