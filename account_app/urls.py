from django.conf.urls import include, url
from django.contrib.admindocs.urls import urlpatterns
from rest_framework import routers
from .views import AuthRegister, AuthInfoGetView

urlpatterns = [
  url(r'^register/$', AuthRegister.as_view()),
  url(r'^mypage/', AuthInfoGetView.as_view()),
]