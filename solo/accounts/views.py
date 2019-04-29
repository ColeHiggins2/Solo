from django.contrib.auth import login, logout
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from . import forms
from django.contrib.auth import get_user_model
from accounts.models import UserProfileInfo as UserProfileInfoModel
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

User = get_user_model()
class People(TemplateView):
    template_name = 'accounts/people.html'
    success_url = reverse_lazy('accounts:people')

    def get(self, request):
        users = UserProfileInfoModel.objects.exclude(user = request.user)
        args = {'users': users}
        return render(request, self.template_name, args)




class Profile_Edit(UpdateView):
    fields = ['image', 'bio','age', 'gender', 'class_year']
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self):
        return self.request.user.userprofileinfo

class SurveyCreation(UpdateView):
    fields = ['smoking','Sleeping_Habits','Dorm_Choice_One', 'Dorm_Choice_Two', 'Dorm_Choice_Three','cleanliness']
    success_url = reverse_lazy('accounts:profile')
    template_name = 'accounts/survey.html'

    def get_object(self):
        return self.request.user.userprofileinfo
