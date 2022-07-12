from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from . import models
def test(request, *args, **kwargs):
    return HttpResponse('200')

def new_question_list_all(request):
    questions = models.Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = 'qa/home/?page='
    page = paginator.page(page) # Page
    return render(request, 'home.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })
def rating_question_list_all(request):
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
def question(request, pk):
    question = get_object_or_404(models.Question, pk=pk)
    return render(request, 'question.html', {
        'question': question
    })


