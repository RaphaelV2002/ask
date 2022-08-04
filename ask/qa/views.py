from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views, login, logout
from django.views.decorators.http import require_GET, require_POST
from . import models
from . import forms

def home(request):
    questions = models.Question.objects.new()
    return render(request, 'home.html', {
        'questions': questions,
    })
def popular(request):
    questions = models.Question.objects.popular()
    return render(request, 'popular.html', {
        'questions': questions,
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

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def load_questions(request, *args, **kwargs):
    """Reterns a portion of questions on ajax request."""
    if is_ajax(request):
        start = request.POST.get('questions_num', '15')
        if start.isdigit():
            start = int(start)
        else:
            start = 15
        questions = models.Question.objects.all()[start:start+15]
        data = []
        for question in questions:
            data.append(question.to_json())
        return JsonResponse({'questions': data}, status=200)
    return JsonResponse({}, status = 500)