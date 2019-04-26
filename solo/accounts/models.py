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
    CLASS_YEAR = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('UU', 'Unspecified'),
    )
    class_year = models.CharField(max_length = 2, choices = CLASS_YEAR, default = 'UU')
    age = models.IntegerField(max_length=2, blank = False, default = 0)
    matching = models.IntegerField(max_length=2, blank = False, default = 0)
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unspecified'),
    )
    gender = models.CharField(max_length = 1, choices = GENDER, default = 'U')
    #favorites = models.TextField(max_length = 100, blank = True)
    SMOKING = (
        ('Y', 'Smoking'),
        ('N', 'No Smoking'),
    )
    smoking = models.CharField(max_length=1, choices=SMOKING, default = 'U')
    BED = (
        ('U', 'Unspecified'),
        ('E', 'Early Riser'),
        ('L', 'Late Riser'),
    )
    Sleeping_Habits = models.CharField(max_length = 1, choices=BED, default = 'U')

    DORM = (
        ('UU', 'Unspecified'),
        ('BE', 'Belk Hall'),
        ('EL', 'Elm Hall'),
        ('GR', 'Greek Village'),
        ('HA', 'Hawthorn Hall'),
        ('HO', 'Holshouser Hall'),
        ('HU', 'Hunt Hall'),
        ('LA', 'Laurel Hall'),
        ('LE', 'Levine Hall'),
        ('LY', 'Lynch Hall'),
        ('MA', 'Martin Hall'),
        ('WI', 'Witherspoon Hall'),
        ('MI', 'Miltimore Hall'),
        ('OA', 'Oak Hall'),
        ('PI', 'Pine Hall'),
        ('SC', 'Scott Hall'),
        ('WA', 'Wallis Hall'),
        ('SA', 'Sanford Hall'),
    )
    Dorm_Choice_One = models.CharField(max_length=3, choices=DORM, default = 'UU')
    Dorm_Choice_Two = models.CharField(max_length=3, choices=DORM, default = 'UU')
    Dorm_Choice_Three = models.CharField(max_length=3, choices=DORM, default = 'UU')

    cleanliness = (
    ('UU', 'Unspecified'),
    ('1', 'One (lowest)'),
    ('2', 'Two'),
    ('3', 'Three'),
    ('4', 'Four'),
    ('5', 'Five (highest)'),
    )
    cleanliness = models.CharField(max_length = 2, choices = cleanliness, default = 'UU')

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
