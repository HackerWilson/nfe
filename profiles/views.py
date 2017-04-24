# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from accounts.models import User


@login_required
def show_profile(request):
    user = request.user
    context = {"user": user}
    return render(request, 'profiles/profile.html', context)
