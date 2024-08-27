from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title      = models.CharField(max_length=40 , unique=True )
    content    = models.TextField(max_length=  40, blank=True  )
    category   = models.CharField(max_length= 40  , blank = True , null=True)
    rating     = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True,auto_created=True,null=True, blank=True)
    user       = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        get_latest_by =  'created_at'
        
    def __str__(self) -> str:
        return self.title

class Answer(models.Model) : 
    user    = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(max_length=  40, blank=True)
    created_at = models.DateTimeField(auto_now=True,auto_created=True)
    question= models.OneToOneField(Question, on_delete=models.PROTECT)
    

    def __str__(self) -> str:
        return str((self.content)[:10])
    