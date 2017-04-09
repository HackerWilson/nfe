from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^record/$', views.list_records, name='feedbacks.list_records'),
    url(r'^behavior/(?P<behavior>\w+)/$', views.list_behavior, name='feedbacks.list_behavior'),
    url(r'^behavior/(?P<behavior>\w+)/lecture/(?P<lecture_id>[0-9]+)/add$', views.add_behavior, name='feedbacks.add_behavior'),
    url(r'^behavior/(?P<behavior_id>[0-9]+)/delete$', views.delete_behavior, name='feedbacks.delete_behavior_by_id'),
    url(r'^behavior/(?P<behavior>\w+)/delete$', views.delete_behavior, name='feedbacks.delete_behavior_by_name'),
    url(r'^comment/user/$', views.list_user_comments, name='feedbacks.list_user_comments'),
    url(r'^comment/lecture/(?P<lecture_id>[0-9]+)/$', views.list_lecture_comments, name='feedbacks.list_lecture_comments'),
    url(r'^comment/lecture/(?P<lecture_id>[0-9]+)/add$', views.add_comment, name='feedbacks.add_comment'),
    url(r'^question/user/$', views.list_questions, name='feedbacks.list_user_questions'),
    url(r'^question/lecture/(?P<lecture_id>[0-9]+)/$', views.list_questions, name='feedbacks.list_lecture_questions'),
    url(r'^question/lecture/(?P<lecture_id>[0-9]+)/add$', views.add_question, name='feedbacks.add_question'),
]
