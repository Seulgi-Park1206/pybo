from django.db import models
from django.contrib.auth.models import User


# table 관련 작업 파일
# Question 테이블 생성   (model: database?)
class Question(models.Model):
    # 글쓴이 ( on_delete=models.CASCADE -> 연결된 모든 것 지워짐)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    # 질문 제목
    subject = models.CharField(max_length=200)
    # 질문 내용
    content = models.TextField()
    # 질문 작성 일시
    create_date = models.DateTimeField()
    # 수정 일시
    modify_date = models.DateTimeField(null=True, blank=True)
    # 추천인
    voter = models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')


class Comment(models.Model): # 댓글
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)