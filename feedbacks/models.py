# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts.models import User
from lectures.models import Lecture


class Comment(models.Model):
    score = models.PositiveSmallIntegerField(_('Score'))
    detail = models.CharField(_('Detail'), max_length=200, blank=True)
    time = models.DateTimeField(_('Time'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    is_visible = models.BooleanField(_('Is Visible'), default=True)

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comment')

    def __unicode__(self):
        return '{user} - comment'.format(user=self.user)


class Question(models.Model):
    detail = models.CharField(_('Detail'), max_length=200)
    time = models.DateTimeField(_('Time'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    is_visible = models.BooleanField(_('Is Visible'), default=True)

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Question')

    def __unicode__(self):
        return '{user} - question'.format(user=self.user)


BEHAVIOR_CHOICES = (
    ('hide', _('Hidden')),
    ('favour', _('Favourite')),
    ('listened', _('Listened')),
)


class Behavior(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    time = models.DateTimeField(_('Time'))
    behavior = models.CharField(
        _('Behavior'),
        max_length=12,
        choices=BEHAVIOR_CHOICES,
    )
    is_visible = models.BooleanField(_('Is Visible'), default=True)

    class Meta:
        index_together = ['user', 'behavior', 'is_visible']
        unique_together = ('user', 'lecture', 'behavior')
        verbose_name = _('Behavior')
        verbose_name_plural = _('Behavior')

    def __unicode__(self):
        return '{user} - {b}'.format(user=self.user, b=self.behavior)
