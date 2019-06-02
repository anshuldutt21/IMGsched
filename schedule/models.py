from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django import forms
from django.dispatch import receiver
# from django.forms import widget
# from django.forms import *
# Create your models here.

USER_ROLE = (
        (1, 'NORMAL USER'),
        (2, 'ADMIN')
)
class UserProfile(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    user_role = models.IntegerField(choices = USER_ROLE,null=True,blank=True)
    user_year = models.IntegerField(null=True,blank=True)

def create_profile(sender,**kwargs):
	# create_user(request)
	if kwargs['created']:
		user_profile = UserProfile.objects.create(username=kwargs['instance'])
		user_profile.save()

post_save.connect(create_profile,sender=User)