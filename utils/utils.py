# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def upload_cardimage(instance, filename):
    '''名片存储路径为/media/images/cards/用户名/图片名'''

    return 'images/cards/{username}/{filename}'.format(
        username=instance.username,
        filename=filename)


def upload_speakerimage(instance, filename):
    '''讲师照片存储路径为/media/images/speakers/讲师名/图片名'''

    return 'images/speakers/{name}/{filename}'.format(
        name = instance.name,
        filename = filename)
