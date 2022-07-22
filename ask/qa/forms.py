# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from . import models
class AskForm(ModelForm):
    class Meta:
        model = models.Question
        fields = ['title', 'text']

class AnswerForm(ModelForm):
    class Meta:
        model = models.Answer
        fields = ['text', 'question']

class LoginForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'password']

