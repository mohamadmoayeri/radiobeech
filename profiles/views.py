from django.shortcuts import render,redirect

# Create your views here.


from django.views.generic.edit import UpdateView,CreateView

from home.models import story

from .models import personal_information,User

from .forms import Form

#from django.views.decorators.cache import cache_page

#from django.core.cache import caches



def add_personal_information(request):
    user=User.objects.get(username=request.user)
    p=personal_information.objects.filter(person=user)
    if p.exists():
        return redirect ("update_personal_information",user.id)
    else:
        return redirect ("create_personal_information",user.id)





class UPDATE_PERSONAL_INFORMATION(UpdateView):

    template_name="update_personal_information.html"
       
    model=personal_information

    fields=['avatar','phone','gender','birthday']

    success_url='/home/profile'

    def get_queryset(self):
         qs=super().get_queryset()
         return qs.filter(person=self.request.user)

    def get_context_data(self, **kwargs):
        user=User.objects.get(username=self.request.user)
        p=personal_information.objects.get(person=user)
        context = super().get_context_data(**kwargs)
        context.update({"p":p})
        return context
    
   


class CREATE_PERSONAL_INFORMATION(CreateView):

    template_name="create_personal_information.html"
      
    model=personal_information

    fields=['avatar','phone','gender','birthday']

    success_url='/home/profile'

    def get_queryset(self):
         qs=super().get_queryset()
         return qs.filter(person=self.request.user)

    def form_valid(self,form):
        user=User.objects.get(username=self.request.user)
        form.instance.person=user
        form.instance.id=user.id
        return super().form_valid(form)
   


#@cache_page(5*60)
def create_story(request):
    
    user=User.objects.get(username=request.user)
    if request.method=="POST":
        f=Form(request.POST,request.FILES)
        if f.is_valid():
           
            story(user=user,title=f.cleaned_data['title'],sound=request.FILES['sound'],
            image=request.FILES['image'],caption=f.cleaned_data['caption']).save()
        
           


            return redirect ("profile")
            
            
        else:
            return render (request,'create_story.html',{'form':f})

        
    elif request.method=="GET":
       
        f=Form()
        
        return render (request,'create_story.html',{'form':f})



class EDIT_PROFILE(UpdateView):

      template_name="edit_profile.html"
      
      queryset = User.objects

      fields=['username','email','first_name','last_name']

      success_url='/home/profile'

      def get_queryset(self):
         qs=super().get_queryset()
         return qs.filter(username=self.request.user)
      
          
       










    












    






