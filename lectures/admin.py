# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Meeting, Lecture, Category, Speaker


@admin.register(Lecture)
class LectureAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = ['time', 'topic', 'info', 'url', 'speaker', 'category', 'meeting', 'is_passed', 'is_finished']
    list_display = ('topic', 'time', 'speaker', 'category', 'meeting', 'is_passed', 'is_finished')
    list_filter = ['category', 'meeting']


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    fields = ['number', 'name', 'time', 'info', 'is_offline']
    list_display = ('number', 'name', 'time', 'is_offline')


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = ['name', ]
    list_display = ('name', )


@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    fields = ['name', 'intro', 'picture']
    list_display = ('name', 'intro')
