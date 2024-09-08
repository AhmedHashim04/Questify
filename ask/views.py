from django.shortcuts import render , redirect ,get_object_or_404
from django.urls import reverse
from .form import AskForm , AnswerForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
# from django.http import JsonResponse
from friend.models import Friend
from .models import Question , Answer 

 
def question_list(request):
        
    if request.method == 'POST':

        search_info = request.POST
        question_contain_word = search_info['search_txt']
        search_from_time = search_info['from']
        search_to_time = search_info['to']
        
        if not search_from_time and not search_to_time :

            a = Question.objects.filter(group=None , content__icontains=question_contain_word   )
            b = Question.objects.filter(group=None , title__icontains=question_contain_word   )
            questions = a.union(b)
            
        elif search_from_time and not search_to_time  :
            a = Question.objects.filter(group=None , content__icontains=question_contain_word,created_at__gte=(search_from_time))
            b = Question.objects.filter(group=None , title__icontains=question_contain_word,created_at__gte=(search_from_time)   )
            questions = a.union(b)
        
        elif not search_from_time and search_to_time  :
            a = Question.objects.filter(group=None , content__icontains=question_contain_word,created_at__lte=(search_to_time))
            b = Question.objects.filter(group=None , title__icontains=question_contain_word,created_at__lte=(search_to_time)   )
            questions = a.union(b)
        
        else :
            a = Question.objects.filter(group=None , content__icontains=question_contain_word,created_at__range=(search_from_time,search_to_time))
            b = Question.objects.filter(group=None , title__icontains=question_contain_word,created_at__range=(search_from_time,search_to_time)   )
            questions = a.union(b)
            
            
    else:
            questions = Question.objects.filter(group=None)
            my_friends = Friend.objects.filter(user=request.user,status="confirmed")

    return render(request,'ask/questions.html',{"my_friends":my_friends,'questions':questions})


@login_required
def question_detail(request, id):
    # TODO: count of people who click to view post

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

@login_required
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

@login_required
def like(request, id ):
    
    question = get_object_or_404(Question, id=id)
    if request.user in question.like.all() :
        question.like.remove(request.user)
    else :
        question.like.add(request.user)

    return redirect(reverse('ask:question_detail', args=[question.id]))
    # return redirect(reverse('ask:question_list'))
@login_required
def like_answer(request, id , qid):
    # TODO: best Answer in the head of answers

    question = get_object_or_404(Question, id=qid)
    answer = get_object_or_404(Answer, id=id)
    
    if request.user in answer.like.all() :
        answer.like.remove(request.user)
    else :
        answer.like.add(request.user)

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
                myform = form.save(commit=False)
                myform_created_at=myform.created_at
                myform.user = request.user
                myform.last_edit = datetime.now()
                myform.created_at = myform_created_at
                myform.save()

                return redirect(('ask:question_detail'),id=question.id)

    else:

        form = AskForm(instance=question)


    return render(request,"ask/edit_question.html",{"form":form})



