from django.urls import path 

from . import views
app_name ="ask"
urlpatterns = [
    path('',views.ask,name='add_question'),
    path('questions/',views.question_list,name='question_list'),
    path('question/<int:id>',views.question_detail,name='question_detail'),

]

