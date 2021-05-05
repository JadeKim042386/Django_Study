from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200) #최대 200자
    content = models.TextField() #글자 수 제한 X
    create_date = models.DateTimeField() #날짜, 시간 관련
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question') #중복x

    def __str__(self):
        return self.subject

class Answer(models.Model):
    # CASCADE = 답변에 연결된 질문이 삭제되면 답변도 함께 삭제
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer') #중복x

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)