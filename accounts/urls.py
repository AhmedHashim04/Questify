from django.urls import path 
from django.contrib.auth import views as views2
from django.urls import path
from . import views
app_name ="accounts"
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('profile/<slug:slug>',views.profile,name='profile'),
    path('profile/edit/<slug:slug>',views.editprofile,name='profile_edit'),
    path("login/", views2.LoginView.as_view(), name="login"),
    path("logout/", views2.LogoutView.as_view(), name="logout"),
    path("password_change/", views2.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/",views2.PasswordChangeDoneView.as_view(),name="password_change_done",),
    path("password_reset/", views2.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/",views2.PasswordResetDoneView.as_view(),name="password_reset_done",),
    path("reset/<uidb64>/<token>/",views2.PasswordResetConfirmView.as_view(),name="password_reset_confirm",),
    path("reset/done/",views2.PasswordResetCompleteView.as_view(),name="password_reset_complete",),
]
