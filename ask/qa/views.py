from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

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
def question(request, id):
    question = get_object_or_404(models.Question, pk=id)
    return render(request, 'question.html', {
        'question': question
    })
@csrf_exempt
def ask(request):
    if request.method == "POST":
        form = forms.AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(reverse('question',  kwargs={'id': question.id}))
    else:
        form = forms.AskForm()
    return render(request, 'ask.html', {
        'form': form
    })

def answer(request):
    if request.method == "POST":
        form = forms.AnswerForm(request.POST)
        if form.is_valid():
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = forms.AnswerForm()
    return render(request, 'answer.html', {
        'form': form
    })
