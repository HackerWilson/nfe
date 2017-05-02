# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from lectures.models import Lecture
from accounts.models import User


class LiveNote(models.Model):
    note = models.CharField(_('Live Note'), max_length=1000)
    is_visible = models.BooleanField(_('Is Visible'), default=True)

    class Meta:
        verbose_name = _('Live Note')
        verbose_name_plural = _('Live Note')

    def __unicode__(self):
        return self.note


class UserLive(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    is_visible = models.BooleanField(_('Is Visible'), default=True)

    class Meta:
        unique_together = ("user", "lecture")
        verbose_name = _('External Live')
        verbose_name_plural = _('External Live')

    def __unicode__(self):
        return '{user} - live'.format(user=self.user)
