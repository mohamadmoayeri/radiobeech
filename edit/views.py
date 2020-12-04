from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic.edit import UpdateView,DeleteView

from home.models import story

from profiles.models import personal_information


class EDIT_STORY(UpdateView):

    template_name="edit.html"

    model=story
    
    fields=['title','caption']

    success_url="/home/profile"

class DELETE_STORY(DeleteView):
     
     model=story

     template_name="delete.html"

     success_url="/home/profile"



    
