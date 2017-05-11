# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.urls import reverse
from django.http import Http404, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import (
    Comment,
    Question,
    Behavior,
    BEHAVIOR_CHOICES
)
from accounts.models import User
from lectures.models import Lecture


def list_records(request):
    user = request.user
    record_list = []
    if user.is_authenticated:
        record_list = Behavior.objects.filter(user__id=request.user.id, behavior='listened', is_visible=True).order_by('-time')[:10]
    context = {'user': user, 'record_list': record_list}
    return render(request, 'records/records.html', context)


@login_required
def list_behavior(request, behavior):
    behavior_dict = {b[0]:b[1] for b in BEHAVIOR_CHOICES}
    if behavior not in behavior_dict:
        raise Http404("{b} behavior list does not exist.".format(b=behavior))

    behavior_name = behavior_dict["{}".format(behavior)]

    behavior_qs = Behavior.objects.filter(user__id=request.user.id, behavior=behavior, is_visible=True)
    behavior_list = behavior_qs.order_by('-time')

    context = {'behavior': behavior, 'behavior_name': behavior_name, 'behavior_list': behavior_list}
    return render(request, 'feedbacks/behaviors.html', context)


@login_required
def add_behavior(request, behavior, lecture_id):
    behavior_dict = {b[0]:b[1] for b in BEHAVIOR_CHOICES}
    if behavior not in behavior_dict:
        raise Http404("{b} behavior does not exist.".format(b=behavior))

    user = get_object_or_404(User, id=request.user.id)
    lecture = get_object_or_404(Lecture, id=lecture_id)
    time = timezone.now()
    Behavior.objects.update_or_create(user=user,
                                      lecture=lecture, behavior=behavior,
                                      defaults={'is_visible': True, 'time': time})
    return JsonResponse({'status': '200'})


@login_required
def delete_behavior(request, behavior_id=None, behavior=None):
    if behavior:
        behavior_dict = {b[0]:b[1] for b in BEHAVIOR_CHOICES}
        if behavior not in behavior_dict:
            raise Http404("{b} behavior does not exist.".format(b=behavior))

        behavior = Behavior.objects.filter(user__id=request.user.id, behavior=behavior, is_visible=True)
        behavior.update(is_visible = False)
    if behavior_id:
        behavior = get_object_or_404(Behavior, pk=behavior_id, user__id=request.user.id)
        behavior.is_visible = False
        behavior.save()
    return JsonResponse({'status': '200'})

def list_lecture_comments(request, lecture_id=None):
    comment_qs = Comment.objects.filter(lecture__id=lecture_id, is_visible=True).order_by('-time')
    context = {'lecture_id': lecture_id, 'comment_list': comment_qs}

    user = request.user
    if user.is_authenticated and user.has_perm('feedbacks.add_comment') and not comment_qs.filter(user=user):
        context['can_add_comment'] = True
    return render(request, 'feedbacks/comments.html', context)


@login_required
def list_user_comments(request):
    comment_list = Comment.objects.filter(user__id=request.user.id, is_visible=True).order_by('-time')
    context = {'comment_list': comment_list}
    return render(request, 'feedbacks/user_comments.html', context)


@login_required
def add_comment(request, lecture_id):
    if not request.user.has_perm('feedbacks.add_comment'):
        return HttpResponseRedirect('root')
    if request.method == 'POST':
        score = request.POST['score']
        detail = request.POST['detail']
        time = timezone.now()
        user = get_object_or_404(User, id=request.user.id)
        lecture = get_object_or_404(Lecture, id=lecture_id)
        Comment.objects.create(score=score, detail=detail, time=time, user=user, lecture=lecture)
        return HttpResponseRedirect(reverse('lectures.lecture_detail', args=[lecture_id]))
    else:
        lecture = get_object_or_404(Lecture, id=lecture_id)
        context = {'lecture': lecture}
        return render(request, 'feedbacks/comment.html', context)


@login_required
def list_questions(request, lecture_id=None):
    if lecture_id:
        question_qs = Question.objects.filter(lecture__id=lecture_id)
    else:
        question_qs = Question.objects.filter(user__id=request.user.id)
    question_list = question_qs.order_by('-time')
    context = {'lecture_id': lecture_id, 'question_list': question_list}
    return render(request, 'feedbacks/user_questions.html', context)


@login_required
def add_question(request, lecture_id):
    if request.method == 'POST':
        detail = request.POST['detail']
        time = timezone.now()
        user = get_object_or_404(User, id=request.user.id)
        lecture = get_object_or_404(Lecture, id=lecture_id)
        Question.objects.create(detail=detail, time=time, user=user, lecture=lecture)
        return HttpResponseRedirect(reverse('lectures.lecture_detail', args=[lecture_id]))
    else:
        lecture = get_object_or_404(Lecture, id=lecture_id)
        context = {'lecture': lecture}
        return render(request, 'feedbacks/question.html', context)
