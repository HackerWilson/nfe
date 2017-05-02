from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^category/$', views.list_categories, name='lectures.list_categories'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.list_categories, name='lectures.list_categories'),
    url(r'^category/(?P<category_id>[0-9]+)/lecture/$', views.list_lectures, name='lectures.list_lectures'),
    url(r'^lecture/(?P<lecture_id>[0-9]+)/$', views.lecture_detail, name='lectures.lecture_detail'),
]
