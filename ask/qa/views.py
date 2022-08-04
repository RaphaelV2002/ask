from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views, login, logout
from django.views.decorators.http import require_GET, require_POST
from . import models
from . import forms

def home(request):
    questions = models.Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = 'question/?page='
    page = paginator.page(page) # Page
    return render(request, 'home.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })
def popular(request):
    questions = models.Question.objects.popular()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = 'qa/popular/?page='
    page = paginator.page(page) # Page
    return render(request, 'popular.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })

def signup(request):
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

def ask(request, *args, **kwargs):
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
    
    question = get_object_or_404(models.Question, pk=kwargs['question_id'])

    answers = question.answers.all()
    if request.method == "POST":
        form = forms.AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question 
            answer.author = request.user
            answer.save()
            return HttpResponseRedirect(reverse('question',  kwargs={'question_id': question.id}) )
    else:
        form = forms.AnswerForm()
    return render(request, 'question.html', {
        'form': form,
        'answers': answers,
        'question': question
    })

@require_POST
def delete_question(request, *args, **kwargs):
    """Deliting of the question and redirect on the main page."""
    models.Question.objects.filter(
        pk=kwargs['question_id'],
        author=request.user
    ).delete()
    return HttpResponseRedirect('/')

def delete_answer(request, *args, **kwargs):
    """Deliting of the answer and redirect on question page."""
    models.Answer.objects.filter(
        pk=kwargs['answer_id'],
        author=request.user
    ).delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def log_out(request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect('/')

