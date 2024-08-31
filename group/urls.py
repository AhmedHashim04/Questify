from django.urls import path 

from . import views
app_name ="group"
urlpatterns = [
    
    path('addgroup/',views.add_group,name='add_group'),
    path('groups/',views.group_list,name='group_list'),
    path('group/<int:id>',views.group_detail,name='group_detail'),
    path('group/<int:id>/join',views.join_group,name='join_group'),


]

