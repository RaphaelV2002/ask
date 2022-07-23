from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from . import models
from . import forms
def test(request, *args, **kwargs):
    return HttpResponse('200')

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


# def signup(request):
#     if request.method == "POST":
#         form = forms.SignUpForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.set_password(form.cleaned_data['password'])
#             post.save()
#             views.LoginView(request, post)
#             return HttpResponseRedirect(reverse('login'))
#     else:
#         form = forms.SignUpForm()
#     return render(request, 'registration/signup.html', {
#         'form': form
#     })









@csrf_exempt
def ask(request):
    if request.method == "POST":
        form = forms.AskForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            # question.author = request.user
            question.save()
            return HttpResponseRedirect(reverse('home',  kwargs={'id': question.id}))
    else:
        form = forms.AskForm()
    return render(request, 'ask.html', {
        'form': form
    })

def answer(request, id):
    question = get_object_or_404(models.Question, pk=id)

    answers = question.answers.all()
    if request.method == "POST":
        form = forms.AnswerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.question = question 
            # post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('home',  kwargs={'id': question.id}) )
    else:
        form = forms.AnswerForm()
    return render(request, 'question.html', {
        'form': form,
        'answers': answers,
        'question': question
    })