from django.shortcuts import render , redirect ,get_object_or_404
from .models import Question , Answer 
from django.urls import reverse
from .form import AskForm , AnswerForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
