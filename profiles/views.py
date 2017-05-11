# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from django.shortcuts import render

from .models import MenuLink


def show_profile(request):
    user = request.user

    menu_list = MenuLink.objects.filter(is_visible=True).order_by('order')
    context = {'user': user, 'menu_list': menu_list}

    if user.is_authenticated:
        if user.first_name and user.last_name:
            context['certified_user'] = True

    return render(request, 'profiles/profile.html', context)
