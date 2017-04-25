# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Avg
from django.shortcuts import render

from .models import Category, Lecture
from feedbacks.models import Comment


def list_categories(request):
    category_list = Category.objects.all()
    context = {'category_list': category_list}
    return render(request, 'lectures/categories.html', context)


def list_lectures(request, category_id):
    lecture_list = Lecture.objects.filter(category__order=category_id, meeting__is_offline=False)\
                       .order_by('-time')\
                       .values('id', 'topic', 'time', 'meeting__number', 'speaker__name', 'speaker__intro', 'speaker__picture')
    print len(lecture_list), lecture_list
    context = {'lecture_list': lecture_list}
    return render(request, 'lectures/lectures.html', context)


def lecture_detail(request, lecture_id):
    user = request.user
    lecture = Lecture.objects.get(id=lecture_id)

    if lecture.is_finished:
        comment_qs = Comment.objects.filter(lecture__id=lecture_id)
        comment_num = comment_qs.count()
        comment_agg =  comment_qs.aggregate(comment_avg_score=Avg('score'))
        context = {'user': user, 'lecture': lecture,
                   'comment_num': comment_num,
                   'comment_avg_score': comment_agg['comment_avg_score']}
    else:
        context = {'user': user, 'lecture': lecture}

    return render(request, 'lectures/lecture.html', context)
