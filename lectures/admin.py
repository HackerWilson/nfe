# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Meeting, Lecture, Category, Speaker


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    fields = ['time', 'topic', 'info', 'url', 'speaker', 'category', 'meeting', 'is_finished']
    list_display = ('topic', 'time', 'speaker', 'category', 'meeting', 'is_finished')


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    fields = ['number', 'time', 'info', 'is_offline']
    list_display = ('number', 'time', 'is_offline')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'order']
    list_display = ('name', 'order')


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    fields = ['name', 'intro', 'picture']
    list_display = ('name', 'intro')
