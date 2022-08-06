from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import views, login, logout
from . import models
from . import forms


def home(request, *args, **kwargs):
    """Загружает главную страницу с списком вопросов отсортированным по времени публикации."""
    questions = models.Question.objects.new()
    return render(request, 'home.html', {
        'questions': questions,
    })


def popular(request, *args, **kwargs):
    """Загружает страницу с списком вопросов."""
    questions = models.Question.objects.popular()
    return render(request, 'popular.html', {
        'questions': questions,
    })


def ask(request, *args, **kwargs):
    """Загружает страницу с формой для создания нового вопроса."""
    if request.method == "POST":
        form = forms.AskForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return HttpResponseRedirect(reverse('question',  kwargs={'question_id': question.id}))
    else:
        form = forms.AskForm()
    return render(request, 'ask.html', {
        'form': form
    })


def question(request, *args, **kwargs):
    """Загружает страницу вопроса с ответами на него и формой для создания ответа"""
    question = get_object_or_404(models.Question, pk=kwargs['question_id'])
    answers = question.answers.all()
    if request.method == "POST":
        form = forms.AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return HttpResponseRedirect(reverse('question',  kwargs={'question_id': question.id}))
    else:
        form = forms.AnswerForm()
    return render(request, 'question.html', {
        'form': form,
        'answers': answers,
        'question': question
    })


def delete_question(request, *args, **kwargs):
    """Удаляет вопрос и направляет на главную страницу"""
    models.Question.objects.filter(
        pk=kwargs['question_id'],
        author=request.user
    ).delete()
    return HttpResponseRedirect('/')


def delete_answer(request, *args, **kwargs):
    """Удаляет ответ и направляет на текущую страницу"""
    models.Answer.objects.filter(
        pk=kwargs['answer_id'],
        author=request.user
    ).delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def signup(request, *args, **kwargs):
    """Загружает страницу с формой для регистрации нового пользователя."""
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('login'))
    else:
        form = forms.SignUpForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


def log_out(request, *args, **kwargs):
    """Выход пользователя."""
    logout(request)
    return HttpResponseRedirect('/')
