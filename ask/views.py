from django.shortcuts import render , redirect ,get_object_or_404
from .models import Question , Answer 
from django.urls import reverse
from .form import AskForm , AnswerForm
from django.contrib.auth.decorators import login_required

 
def question_list(request):
    questions = Question.objects.all()
    
    return render(request,'ask/questions.html',{'questions':questions})


@login_required
def question_detail(request, id):
    question = get_object_or_404(Question, pk=id)
    answers = Answer.objects.filter(question=question)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('ask:question_detail', id=question.pk)
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

def like(request, id):
    question = get_object_or_404(Question, id=id)
    if request.user in question.like.all() :
        question.like.remove(request.user)
    else :
        question.like.add(request.user)

    return redirect(reverse('ask:question_detail', args=[question.id]))

@login_required
def delete_question(request, id):
    question = get_object_or_404(Question, id=id)
    if request.user == question.user :
        question.delete()
        return redirect('ask:question_list')
    return redirect('ask:question_detail', id=question.id)



@login_required
def edit_question(request,id):
    question = get_object_or_404(Question,pk=id)
    if request.method == 'POST':
        if request.user == question.user:
            form = AskForm(request.POST,instance=question)
            if form.is_valid() :
                # form.save()
                myform = form.save(commit=False)
                myform.user = request.user
                myform.save()

                return redirect(('ask:question_detail'),id=question.id)

    else:

        form = AskForm(instance=question)


    return render(request,"ask/edit_question.html",{"form":form})



# @login_required
# def edit_question(request, id):
#     question = get_object_or_404(Question, id=id)

#         return redirect('ask:question_detail', id=question.id)

#     if request.method == "POST":
#         form = QuestionForm(request.POST, instance=question)
#         if form.is_valid():
#             form.save()
#             return redirect('ask:question_detail', id=question.id)
#     else:
#         form = QuestionForm(instance=question)

#     return render(request, 'ask/edit_question.html', {'form': form})