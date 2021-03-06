# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.utils import upload_speakerimage


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=12)
    order = models.PositiveIntegerField(_('Order'), default=0)

    class Meta:
        ordering = ('order', )
        unique_together = ("name", "order")
        verbose_name = _('Lecture Category')
        verbose_name_plural = _('Lecture Category')

    def __unicode__(self):
        return self.name


class Speaker(models.Model):
    name = models.CharField(_('Speaker Name'), max_length=12, unique=True)
    intro = models.CharField(_('Speaker Info'), max_length=200, blank=True)
    picture = models.ImageField(_('Speaker Picture'),
                                upload_to=upload_speakerimage,
                                blank=True)

    class Meta:
        verbose_name = _('Lecture Speaker')
        verbose_name_plural = _('Lecture Speaker')

    def __unicode__(self):
        return self.name


class Meeting(models.Model):
    number = models.PositiveIntegerField(_('Number'), unique=True)
    name = models.CharField(_('Name'), max_length=12, blank=True)
    time = models.DateTimeField(_('Time'))
    info = models.CharField(_('Info'), max_length=1000, blank=True)
    is_offline = models.BooleanField(_('Is Offline'), default=False)

    class Meta:
        ordering = ('number', )
        verbose_name = _('Meeting Info')
        verbose_name_plural = _('Meeting Info')

    def __unicode__(self):
        return _('{num} Meeting').format(num=self.number)


class Lecture(models.Model):
    order = models.PositiveIntegerField(_('Order'), default=0)
    time = models.DateTimeField(_('Time'))
    topic = models.CharField(_('Topic'), max_length=50)
    info = models.TextField(_('Info'), max_length=500, blank=True)
    url = models.URLField(_('URL'), max_length=300, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    speaker = models.ForeignKey('Speaker', on_delete=models.CASCADE)
    meeting = models.ForeignKey('Meeting', on_delete=models.CASCADE)
    is_passed = models.BooleanField(_('Is Passed'), default=True)
    is_finished = models.BooleanField(_('Is Finished'), default=False)

    class Meta:
        ordering = ('order', )
        unique_together = ("topic", "speaker", "meeting")
        verbose_name = _('Lecture Info')
        verbose_name_plural = _('Lecture Info')

    def __unicode__(self):
        return self.topic
