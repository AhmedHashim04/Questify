from .models import Question , Answer
from django import forms




class AskForm(forms.ModelForm):
    class Meta:
        model  = Question
        fields =['title','content','tags',]
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model  = Answer

        fields =['content']



