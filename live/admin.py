# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import LiveNote, UserLive

@admin.register(LiveNote)
class LiveNoteAdmin(admin.ModelAdmin):
    fields = ['note', 'is_visible']
    list_display = ['note', 'is_visible']


@admin.register(UserLive)
class UserLiveAdmin(admin.ModelAdmin):
    fields = ['user', 'lecture', 'is_visible']
    list_display = ['user', 'lecture', 'is_visible']
