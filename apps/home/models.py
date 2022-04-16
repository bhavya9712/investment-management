# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
#

class CustomUser(AbstractUser):
    address = models.CharField(max_length=500,null=True)
    gender = models.CharField(max_length=20,blank=True)
    profilephoto= models.ImageField(upload_to='media/',null=True,blank=True,default="media/OIP_IDXLbG6.jpeg")
    clients_family = models.ManyToManyField('self', symmetrical=False,null=True,blank=True)
