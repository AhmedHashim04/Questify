from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver



# -Profile
class Notification(models.Model):
    
    choices = [
        
            ('friend_accepted','friend_accepted'),
            ('friend_request','friend_request'),
            ('friend_message','friend_message'),
            ('group_joined','group_joined'),
            ('question_answered','question_answered'),
            ('question_liked','question_liked'),
            ('answer_liked','answer_liked'),
            
            ]
    
    from_user = models.ForeignKey(User , on_delete=models.CASCADE,related_name='from_user' )
    to_user   = models.ForeignKey(User , on_delete=models.CASCADE,related_name='to_user' )
    content   = models.CharField(choices=choices, max_length=50) 
    is_read   = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.to_user} - {self.content}"

class Profile(models.Model):
    
    
    user             = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_day        = models.DateTimeField( auto_now=False, auto_now_add=False,null=True,blank=True)
    bio              = models.TextField(max_length=50,null=True,blank=True)
    tel              = models.CharField(max_length=20,null=True,blank=True)
    slug             = models.SlugField(unique=True,blank=True,null=True)
    image            = models.ImageField(upload_to=f"profile_images/", default='assets/avatar.svg', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    waiting_friend   = models.ManyToManyField(User , blank=True ,related_name="waiting_friend")
    confirmed_friend = models.ManyToManyField(User , blank=True ,related_name="confirmed_friend")


    def __str__(self) -> str:
        return self.user.username
    
    def save(self,*args, **kwargs):
        if not self.slug :
            self.slug = slugify(self.user.username)
        super(Profile,self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("accounts:profile", kwargs={"slug": self.slug})
    

    @receiver(post_save, sender=User)
    def create_user_profile(sender, **kwargs):
        if kwargs['created']:
            Profile.objects.create(user=kwargs['instance'])

