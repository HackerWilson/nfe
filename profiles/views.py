# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def show_profile(request):
    user = request.user
    context = {'user': user}

    if user.is_authenticated:
        if user.first_name and user.last_name:
            context = {'user': user, 'certified_user': True}

    return render(request, 'profiles/profile.html', context)
