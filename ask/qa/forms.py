# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.contrib.auth.models import User
from . import models
class AskForm(ModelForm):
    class Meta:
        model = models.Question
        fields = ['title', 'text']

class AnswerForm(ModelForm):
    class Meta:
        model = models.Answer
        fields = ['text']

class LoginForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'password']

class SignUpForm(ModelForm):
    class Meta:
        model = models.User
        fields = ['username', 'email', 'password']
        help_texts = {
            'username': None,
        }