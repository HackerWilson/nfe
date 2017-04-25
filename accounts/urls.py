from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='accounts.login'),
    url(r'^login/auth/$', views.auth, name='accounts.auth'),
]
