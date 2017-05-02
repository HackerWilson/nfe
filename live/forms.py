# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from lectures.models import Lecture, Speaker


class LectureForm(forms.ModelForm):
    speaker_name = forms.CharField(label=_('Speaker Name'), max_length=12)
    speaker_intro = forms.CharField(label=_('Speaker Info'), max_length=200)
    speaker_picture = forms.ImageField(label=_('Speaker Picture'), required=False)

    class Meta:
        model = Lecture
        fields = ['topic', 'time', 'info']
