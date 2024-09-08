from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from group.models import Group 

# Create your models here.
class Question(models.Model):
    title      = models.CharField(max_length=1000 , unique=True )
    content    = models.TextField(max_length=40000, blank=True  )
    rating     = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True,auto_created=True,null=True, blank=True,)
    last_edit  = models.DateTimeField(auto_created=True,null=True, blank=True)
    user       = models.ForeignKey(User,on_delete=models.CASCADE,related_name="Question_user")
    like       = models.ManyToManyField(User , blank=True ,related_name="Question_like")
    group      = models.ForeignKey(Group ,on_delete=models.CASCADE, blank=True ,null=True,related_name="group_question")

    class Meta:
        ordering  = ['-created_at']
        get_latest_by =  'created_at'
        

    def get_absolute_url(self):
        return reverse("ask:question_detail", kwargs={"id": self.pk})
        
    def __str__(self) -> str:
        return self.title

class Answer(models.Model):
    # TODO: most live answer
    user       = models.ForeignKey(User, on_delete=models.CASCADE,related_name="Answer_user")
    content    = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now=True, auto_created=True)
    question   = models.ForeignKey(Question, on_delete=models.CASCADE,related_name="question") 
    like       = models.ManyToManyField(User , blank=True ,related_name="Answer_like")

    class Meta:
        get_latest_by = 'created_at'
        ordering  = ['-created_at']

    def __str__(self) -> str:
        return str(self.content)
