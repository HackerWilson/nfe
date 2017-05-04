# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
import datetime
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import LiveNote, UserLive
from .forms import LectureForm
from accounts.models import User
from lectures.models import Speaker, Category, Meeting, Lecture


def live_note(request):
    user = request.user
    note_list = LiveNote.objects.filter(is_visible=True)
    context = {'note_list': note_list, 'user': user}

    if user.is_authenticated:
        if user.first_name and user.last_name:
            context['certified_user'] = True
            live_list = UserLive.objects.filter(user__id=user.id, is_visible=True)
            context['live_list'] = live_list
            auditing_count = live_list.filter(lecture__is_passed=False).count()
            context['auditing_count'] = auditing_count
    return render(request, 'live/note.html', context=context)

@login_required
def add_live(request, lecture_id=None):
    if request.method == 'POST':
        lecture_form = LectureForm(request.POST, request.FILES)
        t = request.POST['time']
        date = datetime.date.fromtimestamp(time.mktime(time.strptime(t, "%Y-%m-%d")))
        lecture_time = timezone.now().replace(year=date.year, month=date.month, day=date.day)
        topic = request.POST['topic']
        info = request.POST['info']
        speaker_name = request.POST['speaker_name']
        speaker_intro = request.POST['speaker_intro']
        speaker_picture = request.FILES.get('speaker_picture', '')
        if speaker_picture:
            speaker, _ = Speaker.objects.update_or_create(name=speaker_name,
                                                          defaults={'intro': speaker_intro, 'picture': speaker_picture})
        else:
            speaker, _ = Speaker.objects.update_or_create(name=speaker_name,
                                                          defaults={'intro': speaker_intro})

        category = Category.objects.order_by('order').last()
        meeting = Meeting.objects.order_by('id').first()
        lecture, _ = Lecture.objects.update_or_create(topic=topic, speaker=speaker, meeting=meeting,
                                                      defaults={'time': lecture_time, 'info': info,
                                                                'category': category, 'is_passed': False})
        user = get_object_or_404(User, id=request.user.id)
        UserLive.objects.update_or_create(user=user, lecture=lecture)
        return HttpResponseRedirect(reverse('lectures.list_categories', args=[category.order]))
    else:
        context = {}
        if lecture_id:
            lecture_form = LectureForm()
            lecture = get_object_or_404(Lecture, id=lecture_id)
            context['topic'] = lecture.topic
            context['time'] = lecture.time.strftime("%Y-%m-%d")
            context['info'] = lecture.info
            context['speaker_name'] = lecture.speaker.name
            context['speaker_intro'] = lecture.speaker.intro
        else:
            lecture_form = LectureForm()
            user = request.user
            context['speaker_name'] = user.last_name + user.first_name
        context['form'] = lecture_form
        return render(request, 'live/live.html', context=context)
