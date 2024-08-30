from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Group(models.Model):
    leader      = models.OneToOneField(User,on_delete=models.CASCADE,related_name="Leader")
    name        = models.CharField(max_length=50,unique=True)
    bio         = models.TextField(max_length=50,null=True,blank=True)
    members     = models.ForeignKey(User,on_delete=models.PROTECT,related_name="Members")
    created_at  = models.DateTimeField(auto_now=True,auto_created=True,null=True, blank=True)

    class Meta:
        get_latest_by =  'created_at'

    def get_absolute_url(self):
        return reverse("group", kwargs={"id": self.pk})
    
    # def save(self,*args, **kwargs):
    #     if not self.leader :
    #         self.leader = self.user
    #         self.members = self.user
    #     super(Group,self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name