from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Question(models.Model):
    title      = models.CharField(max_length=40 , unique=True )
    content    = models.TextField(max_length=  40, blank=True  )
    category   = models.CharField(max_length= 40  , blank = True , null=True)
    rating     = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True,auto_created=True,null=True, blank=True)
    user       = models.ForeignKey(User,on_delete=models.CASCADE,related_name="Question_user")
    like       = models.ManyToManyField(User , blank=True ,related_name="Question_like")

    class Meta:
        get_latest_by =  'created_at'

    def get_absolute_url(self):
        return reverse("ask:question_detail", kwargs={"id": self.pk})
        
    def __str__(self) -> str:
        return self.title

class Answer(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE,related_name="Answer_user")
    content    = models.TextField(max_length=40, blank=True)
    created_at = models.DateTimeField(auto_now=True, auto_created=True)
    question   = models.ForeignKey(Question, on_delete=models.CASCADE,related_name="question") 
    like       = models.ManyToManyField(User , blank=True ,related_name="Answer_like")

    class Meta:
        get_latest_by = 'created_at'

    def __str__(self) -> str:
        return str(self.content)
