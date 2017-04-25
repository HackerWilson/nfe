# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from utils.utils import upload_cardimage


class User(AbstractUser):
    nickname = models.CharField(_('Nickname'), max_length=30, blank=True)
    headimgurl = models.CharField(_('Head Image URL'), max_length=300, blank=True)
    card = models.ImageField(_('Business Card'),
                             upload_to=upload_cardimage,
                             blank=True)
    company = models.CharField(_('Company Name'), max_length=30, blank=True)
    position = models.CharField(_('Company Position'), max_length=30, blank=True)
