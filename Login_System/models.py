from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
import pytz
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserAccounts(models.Model):
    username=models.CharField(default=None,max_length=500)
    password=models.CharField(default=None,max_length=500)
    email=models.EmailField(default=None)
    cell_no=PhoneNumberField(blank=False)
    user_type=models.CharField(max_length=500,default=None,blank=False)

    first_name=models.CharField(max_length=500,default=None)
    last_name=models.CharField(max_length=500,default=None)
    
    

    login_expire_time=models.DateTimeField(default=None,blank=True)
    login_token=models.CharField(default=None,max_length=1000,blank=True)
    user_status=models.CharField(default=None,max_length=100,blank=True)
    last_login=models.DateTimeField(default=None,max_length=1000,blank=True)



class User_Reg_Types(models.Model):
    type=models.CharField(max_length=500,default=None)
    url=models.CharField(max_length=500,default=None)
    created_at=models.DateTimeField()
    
    def __str__(self):
        return self.type


class User_Login_Types(models.Model):
    #id=models.AutoField()
    type=models.CharField(max_length=500,default=None)
    url=models.CharField(max_length=500,default=None)
    created_at=models.DateTimeField()

    def __str__(self):
        return self.type

class Register_As_Job_Searcher(models.Model):
    f_name=models.CharField(max_length=100,default=None,blank=False)
    l_name=models.CharField(max_length=500,default=None,blank=False)
    highest_qualification=models.CharField(max_length=500,blank=False,default=None)
    branch=models.CharField(max_length=500,default=None)
    user_type=models.CharField(max_length=500,default="job_searcher")
    username=models.CharField(max_length=500,default=None,blank=False)
    password=models.CharField(max_length=100,default=None,blank=False)
    email_id=models.EmailField(blank=False)
    cell_no=PhoneNumberField(blank=False)
    
    
    
    def __str__(self) -> str:
        return self.username

class Register_As_Student(models.Model):
    f_name=models.CharField(max_length=100,default=None,blank=False)
    l_name=models.CharField(max_length=500,default=None,blank=False)
    qualification=models.CharField(max_length=20,blank=False,default=None)
    year=models.CharField(max_length=100,default=None,blank=True)
    sem=models.CharField(max_length=100,default=None,blank=True)
    user_type=models.CharField(max_length=500,default="student",blank=False)
    username=models.CharField(max_length=500,default=None,blank=False)
    password=models.CharField(max_length=100,default=None,blank=False)
    email_id=models.EmailField(blank=False)
    cell_no=PhoneNumberField(blank=False)
    branch=models.CharField(default=None,max_length=200)
    
    
    
    def __str__(self) -> str:
        return self.username

class Register_As_Company(models.Model):
    
    company_name=models.CharField(max_length=100,default=None,blank=False)
    username=models.CharField(max_length=500,default=None,blank=False)
    password=models.CharField(max_length=100,default=None,blank=False)
    email_id=models.EmailField(blank=False)
    cell_no=PhoneNumberField(blank=False)
    f_name=models.CharField(max_length=100,default=None,blank=False)
    l_name=models.CharField(max_length=500,default=None,blank=False)
    user_type=models.CharField(max_length=500,default="company",blank=False)

    
    def __str__(self) -> str:
        return self.company_name
    