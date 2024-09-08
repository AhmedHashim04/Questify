from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_user')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_of_user')
    status = models.CharField(max_length=20, choices=[('waiting', 'Waiting'), ('confirmed', 'Confirmed')])
    timestamp = models.DateTimeField(auto_now_add=True)
    

    
