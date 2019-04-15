from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/',
    auth_views.LoginView.as_view(template_name = 'accounts/login.html'),
    name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('profile/',views.UserProfileInfo.as_view(),name='profile'),
    path('profile/edit/',views.Profile_Edit.as_view(),name='edit_profile')
    ]
