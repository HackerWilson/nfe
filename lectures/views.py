# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Category, Lecture


def list_categories(request):
    category_list = Category.objects.all()
    context = {'category_list': category_list}
    return render(request, 'lectures/categories.html', context)


def list_lectures(request, category_id):
    lecture_list = Lecture.objects.filter(category__order=category_id, meeting__is_offline=False, is_finished=False)\
                       .order_by('-time')\
                       .values('id', 'topic', 'time', 'meeting__number', 'speaker__name', 'speaker__intro', 'speaker__picture')
    context = {'lecture_list': lecture_list}
    return render(request, 'lectures/lectures.html', context)


def lecture_detail(request, lecture_id):
    lecture = Lecture.objects.get(id=lecture_id)
    context = {'lecture': lecture}
    return render(request, 'lectures/lecture.html', context)
