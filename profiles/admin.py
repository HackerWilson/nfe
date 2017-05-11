# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import MenuLink


@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    fields = ['order', 'name', 'url', 'is_visible']
    list_display = ('order', 'name', 'url', 'is_visible')
