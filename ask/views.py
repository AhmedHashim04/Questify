from django.shortcuts import render , redirect ,get_object_or_404
from .models import Question , Answer 
from django.urls import reverse
from .form import AskForm , AnswerForm
from django.contrib.auth.decorators import login_required

 
def question_list(request):
    questions = Question.objects.all()
    
    return render(request,'ask/questions.html',{'questions':questions})


@login_required
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = Answer.objects.filter(question=question)
    
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('ask:question_detail', pk=question.pk)
    else:
        form = AnswerForm()

    return render(request, 'ask/question_detail.html', {'question': question,'answers': answers,'form': form})

def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid() :
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()

            return redirect(reverse('ask:question_list'))
    else:
        form = AskForm()

    return render(request,"ask/ask_question.html",{"form":form})
