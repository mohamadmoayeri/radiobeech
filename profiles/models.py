from django.db import models

# Create your models here.

from django.contrib.auth.models import User
   
from ckeditor.fields import RichTextField

from django.contrib.auth.models import User

from django.utils.timezone import now

from django.core.exceptions import ValidationError

import re

def VALID(value):

  x=re.match('^09\d{9}$',value)

  if x:
    return value
  else:
     raise ValidationError('the phone number is incorrect')



    
class personal_information(models.Model):

  person=models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True,verbose_name='user')

  avatar=models.ImageField(upload_to='avatar',null=True,blank=True)

  phone=models.CharField(max_length=11,null=True,blank=True,validators=[VALID],help_text='example:09121112020')

  g=[('m','Male'),('f','Female'),('c','Costum'),('p','Prefer Not To Say')]

  gender=models.CharField(max_length=20,choices=g,default='m')

  birthday=models.DateField(null=True,blank=True,default=now)



 


  