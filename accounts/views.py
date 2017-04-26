# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urllib2
from urlparse import urlparse
from django.conf import settings
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import User
from wechatpy.oauth import WeChatOAuth

app_id = settings.APP_ID
secret = settings.APP_SECRET
redirect_uri = settings.APP_REDIRECT_URI
scope = 'snsapi_userinfo'
oauth = WeChatOAuth(app_id, secret, redirect_uri, scope=scope)


def login(request):
    query_string = request.META.get('QUERY_STRING', '')
    if not query_string:
        http_referer = request.META['HTTP_REFERER']
        state = urlparse(http_referer).path
    else:
        state = query_string.split('=')[1]
    oauth.state = state
    return HttpResponseRedirect(oauth.authorize_url)


def auth(request):
    code = request.GET.get('code', '')
    state = request.GET.get('state', '')
    r = oauth.fetch_access_token(code)
    username = r['openid']
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        data = oauth.get_user_info(r['openid'], r['access_token'])
        user = User(username=username)
        user.nickname = data['nickname']
        user.headimgurl = data['headimgurl']
        user.save()
    auth_login(request, user)
    return HttpResponseRedirect(state)
