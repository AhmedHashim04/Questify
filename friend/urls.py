from django.urls import path 

from . import views
app_name ="ask"
urlpatterns = [
    
    path('',views.ask,name='add_friend'),
    path('friends/',views.friend_list,name='friend_list'),
    
    # path('friend/<int:id>',views.friend_detail,name='friend_detail'),
    # path('friend/<int:id>/like',views.like,name='friend_like'),
    # path('friend/<int:qid>/likeanswer/<int:id>',views.like_answer,name='like_answer'),
    # path('friend/<int:id>/delete',views.delete_friend,name='delete_friend'),
    # path('friend/edit/<int:id>',views.edit_friend,name='edit_friend'),


]
