from django.shortcuts import render , redirect ,get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Friend


# TODO : Friend : unfriend , add friend  
# TODO : massenger 
# TODO : Notifiacation Like , Answer ,friend requestion, recommend to join group
# TODO : Modify Authentications
# TODO : Make Cover and Avatar to users
# TODO : Searhing enhance

def add_friend(request, friend_id) :
    
    friend = get_object_or_404(Friend, id=friend_id)
    
    if request.method == 'POST' :
        
        if Friend.objects.filter(user=request.user , friend=friend) :
            
            Friend.objects.get(user=request.user , friend=friend).delete()
            Friend.objects.get(user=friend , friend=request.user ).delete()
        
        else : 
            
            Friend.objects.create(user=request.user , friend=friend , status="waiting")
            Friend.objects.create(friend=request.user , user=friend , status="waiting")            
    return redirect(reverse('accounts:profile', friend.id))
    # return redirect(reverse('ask:question_detail', args=[question.id]))




        


    
    
