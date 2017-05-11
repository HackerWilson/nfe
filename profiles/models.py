# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class MenuLink(models.Model):
    order = models.PositiveIntegerField(_('Order'))
    name = models.CharField(_('Menu Name'), max_length=12)
    url = models.URLField(_('Menu URL'), max_length=300, blank=True)
    is_visible = models.BooleanField(_('Is Visible'), default=True)


    class Meta:
        ordering = ('order', )
        verbose_name = _('MenuLink')
        verbose_name_plural = _('MenuLink')

    def __unicode__(self):
        return self.name
