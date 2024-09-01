from django.shortcuts import render , redirect ,get_object_or_404
from .models import Group 
from ask.models import Question
from datetime import datetime
from django.urls import reverse
from .form import AddGroupForm
from ask.form import AskForm
from django.contrib.auth.decorators import login_required

@login_required
def add_group(request):
    if request.method == 'POST':
        form = AddGroupForm(request.POST)

        if form.is_valid() :
        
            myform = form.save(commit=False)
            myform.leader = request.user
            # myform.members = request.user
            myform.save()

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


    return render(request,'group/groups.html',{'mygroups':mygroups,'groups':not_my_groups,'user':request.user})

@login_required
def join_group(request,id):
    group = get_object_or_404(Group, id=id)
    
    if request.user in group.members.all() :
        group.members.remove(request.user)

    else :
        group.members.add(request.user)

    return redirect(reverse('group:group_list'))

@login_required
def group_detail(request,id):
    group = get_object_or_404(Group, id=id)
    question = Question.objects.filter(group=group)
    
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.group = group
            myform.save()
            return redirect('group:group_detail', id=group.id)
    else:
        form = AskForm()
    if request.user in group.members.all():
        return render(request, 'group/group_detail.html', {'group': group,'questions': question,'form': form})
    else:
            return redirect(reverse('group:group_list'))
    

@login_required
def delete_group(request, id):
    group = get_object_or_404(Group, id=id)
    if request.user == group.leader :
        group.delete()
        return redirect('group:group_list')
    return redirect('group:group_detail', id=group.id)



@login_required
def edit_group(request,id):
    group = get_object_or_404(Group,pk=id)
    if request.method == 'POST':

        if request.user == group.leader:
            form = AddGroupForm(request.POST,instance=group)
            if form.is_valid() :
                myform = form.save(commit=False)
                myform.leader = request.user
                myform.last_edit = datetime.now()
                myform.save()

                return redirect(('group:group_detail'),id=group.id)

    else:

        form = AddGroupForm(instance=group)


    return render(request,"group/edit_group.html",{"form":form})


