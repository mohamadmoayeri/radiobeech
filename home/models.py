from django.db import models

# Create your models here.

from django.contrib.auth.models import User

import os

from django.core.exceptions import ValidationError

from ckeditor.fields import RichTextField

from django.contrib.auth.models import User

from django.urls import reverse


def valid(value):
     value=str(value)
     ext=os.path.splitext(value)[1]
     if not ext in ['.mp3']:
          raise ValidationError('unsupported')



class story(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_name='UserToStory')

    title=models.CharField(max_length=150,null=True,blank=True)

    sound=models.FileField(upload_to='story',unique=True,null=False,blank=False,validators=[valid])

    image=models.ImageField(upload_to='image',null=True,blank=True)

    caption=RichTextField(max_length=500,null=True,blank=True)

    created_at=models.DateTimeField(auto_now=False, auto_now_add=True)

    update_at=models.DateTimeField(auto_now=True, auto_now_add=False)

    def get_absolute_url(self):
      return reverse("edit", kwargs={"pk": self.id})
      
    def gett_absolute_url(self):
        return reverse("delete", kwargs={"pk": self.pk})
    

    
