from django.contrib.auth import login, logout
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from . import forms
from django.views.generic import TemplateView
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class UserProfileInfo(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

class Profile_Edit(UpdateView):
    fields = ['image', 'bio']
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self):
        return self.request.user.userprofileinfo

class SurveyCreation(UpdateView):
    fields = ['favorites']
    success_url = reverse_lazy('accounts:survey')
    template_name = 'accounts/survey.html'

    def get_object(self):
        return self.request.user.userprofileinfo
