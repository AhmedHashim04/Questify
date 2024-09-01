from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings






# Create your views here.
def contact(request):
    myinfo = Info.objects.first()
    
    if request.method == "POST" :
        subject =  request.POST['subject']
        Email = request.POST['email']
        Message = request.POST['message']
        send_mail(
           f'{subject}',
           f'{Message}',
            f'{Email}',
            [f'{settings.EMAIL_HOST_USER}'],
            fail_silently=False,
            )

    return render(request,"contact/contact.html",{'myinfo':myinfo})