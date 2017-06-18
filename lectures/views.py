# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Avg
from django.shortcuts import render

from .models import Category, Lecture
from feedbacks.models import Comment, Behavior


def list_categories(request, category_id='1'):
    category_list = Category.objects.all()
    context = {'category_list': category_list}

    if category_id:
        context['category_id'] = category_id
    return render(request, 'lectures/categories.html', context)


def list_lectures(request, category_id):
    lecture_qs = Lecture.objects.filter(category__order=category_id, meeting__is_offline=False)
    user = request.user
    if user.is_authenticated:
        hidden_qs = Behavior.objects.filter(user__id=user.id, behavior='hide', is_visible=True).values_list('lecture__id', flat=True)
        hidden_list = [obj for obj in hidden_qs]
        lecture_qs = lecture_qs.exclude(id__in=hidden_list)

    meeting_dict = {}
    exclude_lecture_list = []
    for lecture in lecture_qs:
        meeting_number = lecture.meeting.number
        if meeting_number not in meeting_dict:
            meeting_dict[meeting_number] = Lecture.objects.filter(meeting__number=lecture.meeting.number).count() - 1
        else:
            exclude_lecture_list.append(lecture.id)

    lecture_qs = lecture_qs.exclude(id__in=exclude_lecture_list)
    lecture_list = lecture_qs.values('id', 'order','topic', 'time', 'meeting__number', 'meeting__name', 'speaker__name', 'speaker__intro', 'speaker__picture')
    context = {'lecture_list': lecture_list, 'meeting_dict': meeting_dict}
    return render(request, 'lectures/lectures.html', context)


def lecture_detail(request, lecture_id):
    user = request.user
    lecture = Lecture.objects.get(id=lecture_id)
    context = {'user': user, 'lecture': lecture}

    if lecture.meeting.name and lecture.is_finished and not lecture.url:
        lecture_qs = Lecture.objects.filter(meeting__number=lecture.meeting.number)
        if lecture_qs.count() > 1:
            lecture_list = lecture_qs.order_by('order')
            lecture_count = lecture_list.count()
            context['lecture_list'] = lecture_list
            context['lecture_count'] = lecture_count - 1

    if lecture.is_finished:
        comment_qs = Comment.objects.filter(lecture__id=lecture_id)
        comment_num = comment_qs.count()
        if comment_num:
            context['comment_num'] = comment_num
            comment_agg = comment_qs.aggregate(comment_avg_score=Avg('score'))
            context['comment_avg_score'] = '{:.1f}'.format(comment_agg['comment_avg_score'])

    return render(request, 'lectures/lecture.html', context)
