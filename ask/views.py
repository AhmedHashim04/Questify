from django.shortcuts import render , redirect ,get_object_or_404
from django.urls import reverse
from .form import AskForm , AnswerForm
from django.contrib.auth.decorators import login_required
from accounts.models import  Notification ,Profile
from group.models import  Group
from datetime import datetime
from django.db.models import Q
from accounts.models import Profile
from .models import Question , Answer 
from taggit.models import Tag
from django.contrib import messages


@login_required
def question_list(request,tag_slug=None):
        
    if request.method == 'POST':
        tag = None
        search_info = request.POST

        
        question_contain_word = search_info.get('search_txt', '')
        search_from_time = search_info.get('from', None)
        search_to_time = search_info.get('to', None)
        questions = Question.objects.filter(group=None)


        
        if question_contain_word:
            questions = questions.filter(
                Q(content__icontains=question_contain_word) |
                Q(title__icontains=question_contain_word) 
            )
        
        if search_from_time:
            questions = questions.filter(created_at__gte=search_from_time)
        
        if search_to_time:
            questions = questions.filter(created_at__lte=search_to_time)
        


    else:
        tag = None
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            questions = Question.objects.filter(group=None,tags__in=[tag])
        else:
            questions = Question.objects.filter(group=None)

        
    groups = Group.objects.all()
    profile   = Profile.objects.get( user = request.user )
    myfriends = profile.confirmed_friend.all()
    


    return render(request,'ask/questions.html',
        {
        "my_friends": myfriends,
        'questions':questions,
        'groups':groups,
        'tag':tag,
        })


@login_required
def question_detail(request, id):
    # TODO: count of people who click to view post

    question = get_object_or_404(Question, pk=id)
    answers = Answer.objects.filter(question=question)

    if request.method == 'POST':
        answer = Answer.objects.create(
            user=request.user,
            question=question,
            content=request.POST['content']
        )
        if question.user != request.user :

            notification = Notification.objects.create( from_user = request.user ,
                                                    to_user = question.user ,
                                                    content="question_answered")

        messages.success(request, 'Answer submitted successfully!')

        return redirect('ask:question_detail', id=question.pk)


    return render(request, 'ask/question_detail.html', {'question': question,'answers': answers})

@login_required
def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid() :
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            messages.success(request, 'Question submitted successfully!')

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
        if question.user != request.user :
            notification = Notification.objects.create( from_user = request.user ,
                                                    to_user = question.user ,
                                                    content="question_liked")
        messages.success(request, 'You liked the question!')
        


    # return redirect(reverse('ask:question_detail', args=[question.id]))
    return redirect(reverse('ask:question_list'))

@login_required
def like_answer(request, id , qid):
    # TODO: best Answer in the head of answers

    question = get_object_or_404(Question, id=qid)
    answer = get_object_or_404(Answer, id=id)
    
    if request.user in answer.like.all() :
        answer.like.remove(request.user)
    else :
        answer.like.add(request.user)
        if answer.user != request.user :
            notification = Notification.objects.create( from_user = request.user ,
                                                    to_user = answer.user ,
                                                    content="answer_liked")
        messages.success(request, 'You liked the answer!')

    return redirect(reverse('ask:question_detail', args=[question.id]))

@login_required
def delete_question(request, id):
    question = get_object_or_404(Question, id=id)
    if request.user == question.user :
        question.delete()
        messages.success(request, 'You delete question!')

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
                messages.success(request, 'You edit question!')
                

                return redirect(('ask:question_detail'),id=question.id)

    else:

        form = AskForm(instance=question)


    return render(request,"ask/edit_question.html",{"form":form})



