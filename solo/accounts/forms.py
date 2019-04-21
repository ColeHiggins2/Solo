from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import UserProfileInfo
from accounts.models import UserProfileInfo
from django import forms


class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email','first_name', 'last_name', 'password1', 'password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'



"""class UserSurveyForm(forms.Form):

    class Meta:
        fields = ('username', 'email','first_name', 'last_name', 'password1', 'password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['favorite'].label = 'My Favorites'"""
