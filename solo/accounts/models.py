from django.db import models
from django import forms
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)


User = get_user_model()
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=1000, blank=True)
    favorites = models.TextField(max_length = 100, blank = True)


    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfileInfo.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

#User = get_user_model()
#class UserSurveyInfo(models.Model):
#    username = models.TextField(max_length=20, blank=True)
#    favorites = models.TextField(max_length=100, blank=True)
