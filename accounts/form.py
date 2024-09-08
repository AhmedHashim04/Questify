from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2','email']



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birth_day','bio','tel','image','cover']




