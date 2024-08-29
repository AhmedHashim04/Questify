from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver



# -Profile

class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_day   = models.DateTimeField( auto_now=False, auto_now_add=False,null=True,blank=True)
    bio         = models.TextField(max_length=50,null=True,blank=True)
    tel         = models.CharField(max_length=20,null=True,blank=True)
    image       = models.ImageField(upload_to="profile_image", height_field=None, width_field=None, max_length=None,null=True,blank=True)
    slug        = models.SlugField(unique=True,blank=True,null=True)
    # country

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