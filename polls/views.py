from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question,Choice
from django.urls import reverse

def index(request):
    latest_question_list=Question.objects.all()
    context={'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html',context)

