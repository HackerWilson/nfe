# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Comment, Question, Behavior


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ['score', 'detail', 'time', 'user', 'lecture', 'is_visible']
    list_display = ['score', 'lecture', 'user', 'time', 'is_visible']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['detail', 'time', 'user', 'lecture', 'is_visible']
    list_display = ['lecture', 'user', 'time', 'is_visible']

@admin.register(Behavior)
class BehaviorAdmin(admin.ModelAdmin):
    fields = ['lecture', 'user', 'time', 'behavior', 'is_visible']
    list_display = ['lecture', 'user', 'time', 'behavior', 'is_visible']
