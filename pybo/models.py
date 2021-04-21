from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200) #최대 200자
    content = models.TextField() #글자 수 제한 X
    create_date = models.DateTimeField() #날짜, 시간 관련

    def __str__(self):
        return self.subject

class Answer(models.Model):
    # CASCADE = 답변에 연결된 질문이 삭제되면 답변도 함께 삭제
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()