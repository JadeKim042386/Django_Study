from django.urls import path

from . import views  #from . : 현재 패키지를 가리킴

urlpatterns = [
    path('', views.index),
]