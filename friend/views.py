from django.shortcuts import render , redirect ,get_object_or_404
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from datetime import datetime
from accounts.models import Profile , Notification
from .models import Message
from django.contrib import messages


# TODO : group_quit , member-quit , qroup enhance
# TODO : Notifiacation Like , Answer , recommend to join group , massenger -notification 
# TODO : Modify Authentications
# TODO : Make Cover and Avatar to users
# TODO : Searhing enhance

@login_required
def add_friend(request, slug) :
    
    profile = get_object_or_404(Profile, slug=slug)
    
    me = get_object_or_404(Profile, user = request.user)
    
    if request.user in profile.waiting_friend.all() :
    
        profile.waiting_friend.remove(request.user)
        # me.waiting_friend.remove(profile.user)
        notification = Notification.objects.filter( to_user = profile.user , from_user = request.user , content="friend_request").delete()

         
        
        
    elif request.user in profile.confirmed_friend.all() :
        
        profile.confirmed_friend.remove(request.user)
        # me.confirmed_friend.remove(profile.user)
        
    else : 
        profile.waiting_friend.add(request.user)
        # me.waiting_friend.add(profile.user)
        notification = Notification.objects.create( from_user = request.user , to_user = profile.user , content="friend_request")
        
    messages.success(request, 'Friend request sent successfully!')

          
    return redirect(('accounts:profile'),slug=profile.slug)

@login_required
def accept_friend(request,slug):
    profile = get_object_or_404(Profile, slug=slug)
    me = get_object_or_404(Profile, user = request.user)
    
    # profile.waiting_friend.remove(request.user)
    me.waiting_friend.remove(profile.user)
    
    profile.confirmed_friend.add(request.user)
    me.confirmed_friend.add(profile.user)

    notification = Notification.objects.create( from_user = request.user , to_user = profile.user , content="friend_accepted")
    notification = Notification.objects.filter( to_user = request.user , from_user = profile.user , content="friend_request").delete()
    notification = Notification.objects.create( to_user = request.user , from_user = profile.user , content="friend_accepted",is_read=True)
    messages.success(request, 'Friend accepted  successfully!')

    return redirect(('accounts:profile'),slug=profile.slug)

@login_required
def un_friend(request,slug):
    print('and')
    profile = get_object_or_404(Profile, slug=slug)
    me = get_object_or_404(Profile, user = request.user)
    
    me.confirmed_friend.remove(profile.user)
    profile.confirmed_friend.remove(request.user)
    messages.success(request, 'Friend deleted successfully!')

    
    return redirect(('accounts:profile'),slug=profile.slug)

@login_required
def friend_list(request):
    me = get_object_or_404(Profile, user = request.user)
    friends = me.confirmed_friend.all()    
    return render(request, 'friend/friend_list.html',{'friend_list': friends})


@login_required
def add_message_list(request,slug):
    friend = get_object_or_404(Profile, slug=slug)
    me      = get_object_or_404(Profile, user = request.user)
    friends = me.confirmed_friend.all()    

    if friend.user in me.confirmed_friend.all():
        messages_list1 = Message.objects.filter(from_user  = request.user , to_user=friend.user)
        messages_list2 = Message.objects.filter(to_user  = request.user , from_user=friend.user)
        chat_messages  = messages_list1.union(messages_list2)       
    else :
            return redirect(('accounts:profile'),slug=slug)

    if request.method == 'POST':    
        addmessage = Message.objects.create(
            from_user=request.user,
            to_user=friend.user,
            content=request.POST['content']
            
        )
        notification = Notification.objects.create( from_user = request.user , to_user = friend.user , content="friend_message" ,is_read=False)

    return render(request, 'friend/messages.html',
                  {
                    'chat_messages': chat_messages,
                    "friend":friend,
                    "friends":friends
                    })

         