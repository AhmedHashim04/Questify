from django.shortcuts import render , redirect ,get_object_or_404
from .models import Group 
from django.urls import reverse
from .form import AddGroupForm
from django.contrib.auth.decorators import login_required


def add_group(request):
    if request.method == 'POST':
        form = AddGroupForm(request.POST)
        if form.is_valid() :
            myform = form.save(commit=False)
            myform.leader = request.user
            myform.members = request.user
            myform.save()

            return redirect(reverse('group:groups'))
    else:
        form = AddGroupForm()

    return render(request,"group/add_group.html",{"form":form})



def group_list(request):
    groups = Group.objects.all()

    return render(request,'group/groups.html',{'groups':groups})

def join_group(request):pass
def group_detail():pass