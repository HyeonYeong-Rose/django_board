from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200) #글자수 제한
    content = models.TextField() #글자수 제한없음
    create_date = models.DateTimeField() #작성일시

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #ForeignKey로 질문이 사라지면 답변도 사라지게 속성으로 연결.

    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content