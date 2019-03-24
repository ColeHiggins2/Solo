from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
