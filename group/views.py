from django.shortcuts import render , redirect ,get_object_or_404
from .models import Group 
from ask.models import Question
from accounts.models import  Notification ,Profile
from datetime import datetime
from django.urls import reverse
from .form import AddGroupForm
from ask.form import AskForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages


@login_required
def add_group(request):
    if request.method == 'POST':
        form = AddGroupForm(request.POST)

        if form.is_valid() :
        
            myform = form.save(commit=False)
            myform.leader = request.user
            myform.save()
            myform.members.add( request.user)
            messages.success(request, 'group successfully publishe!')

            return redirect(reverse('group:group_list'))
    else:
        form = AddGroupForm()

    return render(request,"group/add_group.html",{"form":form})

@login_required
def group_list(request):
    groups = Group.objects.all().order_by('created_at')

    mygroups=[]
    for group in groups : 
        if request.user in group.members.all() :
            mygroups.append(group)
    
    not_my_groups=[]
    for group in groups : 
        if request.user not in group.members.all() :
            not_my_groups.append(group)


    return render(request,'group/groups.html',{'mygroups':mygroups,'groups':groups,'user':request.user})

@login_required
def join_group(request,id):
    group = get_object_or_404(Group, id=id)
    
    if request.user in group.members.all() :
        group.members.remove(request.user)
    
    elif request.user  not in group.black_list.all() :
        group.members.add(request.user)
        if group.leader != request.user :
            notification = Notification.objects.create( from_user = request.user ,
                                            to_user = group.leader ,
                                            content="group_joined")
            
        messages.success(request, 'You had joined the group!')

    return redirect(reverse('group:group_list'))

@login_required
def group_detail(request,id):
    group = get_object_or_404(Group, id=id)
    
    if request.method == 'POST': 

        if "title" in (request.POST.keys()) :
            form = AskForm(request.POST)
            if form.is_valid():
                myform = form.save(commit=False)
                myform.user = request.user
                myform.group = group
                myform.save()
                return redirect('group:group_detail', id=group.id)
            else:
                form = AskForm()

        else :
            form = AskForm()
            search_info = request.POST
            question_contain_word = search_info['search_txt']
            search_from_time = search_info['from']
            search_to_time = search_info['to']
            questions = Question.objects.filter(group=group)
            if question_contain_word:
                questions = questions.filter(
                    Q(content__icontains=question_contain_word) |
                    Q(title__icontains=question_contain_word) 
            )
        
        if search_from_time:
            questions = questions.filter(created_at__gte=search_from_time)
        
        if search_to_time:
            questions = questions.filter(created_at__lte=search_to_time)
        

        #fulter end        
            
        if request.user in group.members.all():

                return render(request, 'group/group_detail.html', {'group': group,'questions': question,'form': form})

        else:
                return redirect(reverse('group:group_list'))

    else :
        form = AskForm()
        question = Question.objects.filter(group=group)

        if request.user in group.members.all():

            return render(request, 'group/group_detail.html', {'group': group,'questions': question,'form': form})

        else:
                return redirect(reverse('group:group_list'))
    

@login_required
def delete_group(request, id):
    group = get_object_or_404(Group, id=id)
    if request.user == group.leader :
        group.delete()
        messages.info(request, 'You have deleted the group!')
        return redirect('group:group_list')

    return redirect('group:group_detail', id=group.id)


@login_required
def edit_group(request,id):
    group = get_object_or_404(Group,pk=id)
    if request.method == 'POST':

        if request.user == group.leader:
            form = AddGroupForm(request.POST,instance=group)
            if form.is_valid() :
                created_time = group.created_at 
                myform = form.save(commit=False)
                myform.leader = request.user
                myform.last_edit = datetime.now()
                myform.created_at = created_time
                myform.save()
                messages.success(request, 'You have edit the group!')
                

                return redirect(('group:group_detail'),id=group.id)

    else:

        form = AddGroupForm(instance=group)


    return render(request,"group/edit_group.html",{"form":form})


def block_unblock_member(request,slug,id):
    group = get_object_or_404(Group,pk=id)
    profile = Profile.objects.filter( slug = slug )
    
    if request.user == group.leader :
        group.black_list.add(profile.user)
        group.members.remove(profile.user)
        return redirect('group:block_unblock_member', id=group.id)
        
    elif request.user == group.leader :
        group.black_list.remove(profile.user)
        group.members.add(profile.user)
        
        return redirect('group:block_unblock_member', id=group.id)
        
    return render(request,"group/black_list.html",{"group":group})


