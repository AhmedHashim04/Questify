
    
from django.shortcuts import render , redirect
from accounts.models import Notification,Profile



def notification_view(request):
  
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(to_user=request.user, is_read=True)
        not_read_notifications = Notification.objects.filter(to_user=request.user , is_read=False)
        count = not_read_notifications.count()
        return {'notification_count': count,"my_notifications": notifications,"not_read_notifications": not_read_notifications}
    else:
        count = 0
    return {'notification_count': count}
        
  
  
def mark_notifications_as_read(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Notification.objects.filter(to_user=request.user, is_read=False).update(is_read=True)
        return render(request,'notifications.html')
    return render(request,'notifications.html')
        
def mark_notification_read(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Notification.objects.filter(pk=id).update(is_read=True)
        return render(request,'notifications.html')
    return render(request,'notifications.html')
        

def delete_notification(request,id):
    if request.user.is_authenticated:
        Notification.objects.filter(pk=id).delete()
        
    return redirect('notification')
