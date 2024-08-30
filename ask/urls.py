from django.urls import path 

from . import views
app_name ="ask"
urlpatterns = [
    
    path('',views.ask,name='add_question'),
    path('questions/',views.question_list,name='question_list'),
    path('question/<int:id>',views.question_detail,name='question_detail'),
    path('question/<int:id>/like',views.like,name='question_like'),
    path('question/<int:id>/delete',views.delete_question,name='delete_question'),
    path('question/edit/<int:id>',views.edit_question,name='edit_question'),


]

# The included URLconf '14' does not appear to have any patterns in it. If you see the 'urlpatterns' variable with valid patterns in the file then the issue is probably caused by a circular import.
# 'ManyRelatedManager' object has no attribute 'delete'
