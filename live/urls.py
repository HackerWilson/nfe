from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^note/$', views.live_note, name='live.live_note'),
    url(r'^add/$', views.add_live, name='live.add_live'),
    url(r'^add/(?P<lecture_id>[0-9]+)/$', views.add_live, name='live.add_live'),
]
