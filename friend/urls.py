from django.urls import path 

from .views import add_friend


app_name ="friend"


urlpatterns = [
    
    path('<int:id>/add',add_friend,name='add_friend'),
    
]
