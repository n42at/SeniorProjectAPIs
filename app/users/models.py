from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,AbstractBaseUser,PermissionsMixin
from typing import Optional
# Create your models here.

class User(AbstractUser):
    name =models.CharField(max_length=255)
    email=models.CharField(max_length=255, unique = True)
    password = models.CharField(max_length = 255)
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
class Patient(models.Model):
    Pname =models.CharField(max_length=255)
    PNational_ID =models.CharField(max_length=255, unique = True)
    Mobile_Number = models.CharField(max_length=20,unique = True)
    Scans = None
    
    
class Scan(models.Model):
    Pname =models.CharField(max_length=255)
    PNational_ID =models.CharField(max_length=255, unique = True)
    Mobile_Number = models.CharField(max_length=20,unique = True)
    Scans = None

    # def get_by_natural_key(self, mobile_no_):
    #     print(mobile_no_)
    #     return self.get(mobile_no=mobile_no_)
    
    
    

