from django.urls import path

from . import views  #from . : 현재 패키지를 가리킴

app_name = 'pybo'

urlpatterns = [
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]