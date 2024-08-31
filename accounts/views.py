from django.shortcuts import render , redirect
from django.urls import reverse
from django.contrib.auth import authenticate , login
from .form import SignUpForm ,ProfileForm ,UserForm
from .models import Profile 
from ask.models import  Question ,Answer
from group.models import  Group
from django.contrib.auth.decorators import login_required 
from django.shortcuts import get_object_or_404


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid() :
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password2']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect(reverse('ask:question_list'))
    else:
        form = SignUpForm()

    return render(request,"registration/signup.html",{"form":form})

@login_required
def profile(request,slug):
    profile   = get_object_or_404(Profile,slug=slug)
    myposts   = Question.objects.filter(user=request.user).all()[0:3]
    myanswers = Answer.objects.filter(user=request.user).all()[0:3]
    groups = Group.objects.all()

    mygroups=[]
    for group in groups : 
        if request.user in group.members.all() :
            mygroups.append(group)
    
    return render(request,"registration/profile.html",{"profile":profile,'mygroups':mygroups,'myposts':myposts,'myanswers':myanswers})
    # return render(request,"registration/profile.html",{"profile":profile},{'myposts':myposts})


@login_required
def editprofile(request,slug):
    profile = get_object_or_404(Profile,slug=slug)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST,request.FILES,instance=profile)
        user_form = UserForm(request.POST,instance=request.user)
        if user_form.is_valid() and profile_form.is_valid() :
            user_form.save()
            myprofile_form = profile_form.save(commit=False)
            myprofile_form.user = request.user
            myprofile_form.save()

            return redirect(('accounts:profile'),slug=profile.slug)

    else:

        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)


    return render(request,"registration/profile_edit.html",{"profile_form":profile_form,'user_form':user_form})

