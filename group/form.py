from .models import Group 
from django import forms



class AddGroupForm(forms.ModelForm):
    class Meta:
        model  = Group
        fields =['name']
        




