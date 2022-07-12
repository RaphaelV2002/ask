from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from django.core.paginator import Paginator
from . import views
from . import models
def test(request, *args, **kwargs):
    return HttpResponse('200')

def question_list_all(request):
    questions = models.Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = 'qa/all_questions/?page='
    page = paginator.page(page) # Page
    return render(request, '/home/box/web/ask/qa/question_by_new.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })

