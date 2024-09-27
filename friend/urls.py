from django.urls import path 

from .views import add_friend , accept_friend , friend_list ,un_friend , add_message_list


app_name ="friend"


urlpatterns = [
    
    path('<str:slug>/add',add_friend,name='add_friend'),
    path('<str:slug>/accept',accept_friend,name='accept_friend'),
    path('friends/list',friend_list,name='friend_list'),
    path('<str:slug>/delete',un_friend,name='un_friend'),
    path('chat/<str:slug>',add_message_list,name='chat'),
    
]
