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
    #{u'access_token': u'2R3JSKPL-XjGcbBU2fTBZAGEVWQ-kXqWDE9e3dOsC-YsEOYZgnKQTxxAfyQuoM2CwEST5Kdb9dnxIYWHdnJOcA2drpZeQ8JNzPsancs5D3E', u'openid': u'oaf1QuD6iiBNehuWiKzEYgcdjxg0', u'expires_in': 7200, u'refresh_token': u'aSl4OKU73rsbAmaDxR0IVtJN7cXeaw6R4LdW9pfId4kTgg4lmrxbBqbCe5oYiqCkA9KU2bEwDrVYeoRNIjY1wB0oJ6SpFyzjkmgU_FqupA0', u'scope': u'snsapi_userinfo'}
    #{u'province': u'\u5e7f\u4e1c', u'openid': u'oaf1QuD6iiBNehuWiKzEYgcdjxg0', u'headimgurl': u'http://wx.qlogo.cn/mmopen/4QtDCkraacPzYH5TCf8ibIK9wWV9NOHKVSxovhY2OFD3fUjUIBrMppDiaTqKlF7vXFvxNtdJTBQxZkWrBCs99Gl3Twib8PbC3vL/0', u'language': u'zh_CN', u'city': u'\u5e7f\u5dde', u'country': u'\u4e2d\u56fd', u'sex': 1, u'privilege': [], u'nickname': u'Wilson'}
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
