# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from . import models
class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    # def clean_text(self):
    #     text = self.cleaned_data['text']
    #     if not text.is_valid():
    #         raise forms.ValidationError(
    #             u'Сообщение не корректно', code=12)
    #     return text + \
    #             "\nThank you for your attention."
    def save(self):
        question = models.Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(ModelForm):
    class Meta:
        model = models.Answer
        fields = ['text', 'question']

