from django.shortcuts import render , redirect
from django.urls import reverse
from django.contrib.auth import authenticate , login
from .form import SignUpForm ,ProfileForm ,UserForm
from .models import Profile 
from ask.models import  Question ,Answer
from group.models import  Group
from django.contrib.auth.decorators import login_required 
from django.shortcuts import get_object_or_404
from django.contrib import messages



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
            messages.success(request, 'Welcome In Questify , Account successfuly made !!')

            return redirect(reverse('ask:question_list'))
    else:
        form = SignUpForm()

    return render(request,"registration/signup.html",{"form":form})

@login_required
def profile(request,slug):
    profile   = get_object_or_404(Profile,slug=slug)
    friends   = profile.confirmed_friend.all()    

    myposts   = Question.objects.filter(user=profile.user,group=None).all()[0:3]
    myanswers = Answer.objects.filter(user=profile.user).all()
    
    if request.user in profile.waiting_friend.all() and request.user not in profile.confirmed_friend.all() :
        status = "waiting"
        
    elif request.user in (profile.confirmed_friend.all() and profile.waiting_friend.all()) :
        profile.waiting_friend.remove(request.user)
        status = "confirmed"
        
    elif request.user in profile.confirmed_friend.all() :
        status = "confirmed"
        
    else :
        status = "not_sended"
            
        
    

    a = Group.objects.filter(leader = request.user)
    b = Group.objects.filter( members__exact =  profile.user )
    groups = a.union(b)
    
    return render(request,"registration/profile.html",
                  
                  { 'friends':friends, 'friending_status':status, 'my_user':request.user, 
                     'profile':profile, 'mygroups':groups, 'questions':myposts, 'answers':myanswers })


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
            messages.success(request, 'Profile updated successfully!')
            

            return redirect(('accounts:profile'),slug=profile.slug)

    else:

        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)


    return render(request,"registration/profile_edit.html",{"profile_form":profile_form,'user_form':user_form})

