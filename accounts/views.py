# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urllib2
from django.conf import settings
from django.shortcuts import render
from django.http import Http404, JsonResponse, HttpResponseRedirect

from wechatpy.oauth import WeChatOAuth


def simple_login(request):
    query_string = request.META.get('QUERY_STRING', 'next=/')
    state = query_string.split('=')[1]

    app_id = settings.APP_ID
    secret = settings.APP_SECRET
    redirect_uri = settings.APP_REDIRECT_URI
    oauth = WeChatOAuth(app_id, secret, redirect_uri, state)

    context={"authorize_url": oauth.authorize_url}
    return render(request, 'accounts/simple_login.html', context)


def auth(request):
    code = request.GET.get('code', '')
    state = request.GET.get('state', '')
    print code, state
    return
