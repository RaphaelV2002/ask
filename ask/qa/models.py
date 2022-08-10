# qa/models.py
from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager): 
    def new(self):
        return self.order_by('-added_at')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=50)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
