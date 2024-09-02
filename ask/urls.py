from django.urls import path 

from . import views
app_name ="ask"
urlpatterns = [
    
    path('',views.ask,name='add_question'),
    path('questions/',views.question_list,name='question_list'),
    path('question/<int:id>',views.question_detail,name='question_detail'),
    path('question/<int:id>/like',views.like,name='question_like'),
    path('question/<int:qid>/likeanswer/<int:id>',views.like_answer,name='like_answer'),
    path('question/<int:id>/delete',views.delete_question,name='delete_question'),
    path('question/edit/<int:id>',views.edit_question,name='edit_question'),


]
