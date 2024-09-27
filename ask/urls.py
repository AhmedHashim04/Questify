from django.urls import path 
from . import views
app_name ="ask"
urlpatterns = [
    
    path('add/',views.ask,name='add_question'),
    path('',views.question_list,name='question_list'),
    path('tag/<slug:tag_slug>',views.question_list,name='question_list_by_tag'),
    path('question/<int:id>',views.question_detail,name='question_detail'),
    path('question/<int:id>/like',views.like,name='question_like'),
    path('question/<int:qid>/likeanswer/<int:id>',views.like_answer,name='like_answer'),
    path('question/<int:id>/delete',views.delete_question,name='delete_question'),
    path('question/edit/<int:id>',views.edit_question,name='edit_question'),



]
