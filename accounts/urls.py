from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/simple/$', views.simple_login, name='accounts.simple_login'),
    url(r'^login/simple/auth/$', views.auth, name='accounts.auth'),
]
