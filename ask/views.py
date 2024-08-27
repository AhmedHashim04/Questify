from django.shortcuts import render , redirect
from .models import Question , Answer
from .form import AskForm
 
def question_list(request):
    questions = Question.objects.all()
    for question in questions:
        print (question.content)
    
    return render(request,'ask/questions.html',{'questions':questions})

def question_detail(request,id):
    question = Question.objects.get(id=id)
    return render(request,'ask/question_detail.html',{'question':question})


def ask(request):
    if request.method == 'POST':
        form = AskForm()
        if form.is_valid() :
            form = AskForm(request.POST)
            form.user = request.user
            form.save()

            return redirect("/questions/")
    else:
        form = AskForm()

    return render(request,"ask/ask_question.html",{"form":form})