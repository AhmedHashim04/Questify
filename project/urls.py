"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import handel404 , handel500

from .notification_context import mark_notifications_as_read , delete_notification  , mark_notification_read

urlpatterns = [
    path('accounts/', include('accounts.urls',namespace='accounts')),
    path('', include('ask.urls',namespace='ask')),
    path('admin/', admin.site.urls),
    path('group/', include('group.urls',namespace='group')),
    path('friend/', include('friend.urls',namespace='friend')),
    path('contact/', include('contact.urls',namespace='contact')),
    path('notification/', mark_notifications_as_read, name='notification' ),
    path('notification/<int:id>/delete', delete_notification, name='notification_button' ),
    path('notification/<int:id>/read', mark_notification_read, name='notification_read' ),


    ]

handlr404 = 'project.views.handel404'
handlr500 = 'project.views.handel500'

