from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Message(models.Model):
    from_user     = models.ForeignKey(User , on_delete=models.PROTECT ,related_name="message_from_user")
    to_user       = models.ForeignKey(User , on_delete=models.PROTECT,related_name="message_to_user")
    content       = models.TextField(max_length=1000)
    readed_time   = models.DateTimeField(auto_now=True)
    sended_time  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'From : {self.from_user} | To : {self.to_user}  '
    

