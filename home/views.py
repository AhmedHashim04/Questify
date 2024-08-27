from django.shortcuts import render
# from ..ask.models import Question
from ask.models import Question
import datetime
# Create your views here.

def home(request):
    lastest_questions = Question.objects.latest()
      
    return render(request,'home/home.html',{'lastest_questions':lastest_questions})