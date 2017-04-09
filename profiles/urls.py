from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.show_profile, name='profiles.show_profile'),
]
