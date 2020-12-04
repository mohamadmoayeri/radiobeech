from django.shortcuts import render

# Create your views here.
from .models import story,User

from profiles.models import personal_information


from django.views.generic import ListView,TemplateView

from django.views.generic.edit import FormMixin

from .forms import SEARCH

from django.db.models import Q

class HOME(TemplateView):

    def get(self,request):
        u=[] 
        l=[]    

        for j in story.objects.all():
            l.append(j.user)

        for i in User.objects.all(): 
            u.append({
                'name':i.username,
                'count':l.count(i),
                'avatar':personal_information.objects.filter(person=i)[0].avatar.url if personal_information.objects.filter(person=i).exists() else " "
            })

        u.sort(reverse=True , key=lambda x:x['count'])
        data=[]
        s=story.objects.all()[0:6]
        for i in s:
            data.append({
                'name':i.user.username,
                'title':i.title,
                'sound':i.sound,
                'image':i.image,
                'date':i.created_at.date,

            })

        
        context={
                'count_data':u[0:6],'data':data
        }
        

        return render(request,'registration/index.html',context)

  

class PROFILE(FormMixin,ListView):

    template_name='profile.html'

    model=story

    paginate_by=7
    
    form_class=SEARCH

    def get_queryset(self):
        qs=super().get_queryset()
        if 'search' in self.request.GET:
                f=SEARCH(self.request.GET)

                if f.is_valid():
                    cd=f.cleaned_data['search']

                    return qs.filter(Q(user__exact=self.request.user)&Q(title__icontains=cd)|Q(caption__icontains=cd)).order_by('-created_at')
                    #|Q(user__username__icontains=cd))

        else:

                return qs.filter(user=self.request.user).order_by('-created_at')

    

    def get_context_data(self, **kwargs):
        user=User.objects.get(username=self.request.user)
        p=personal_information.objects.filter(person=user)[0] if personal_information.objects.filter(person=user) else ""
        s=story.objects.filter(user=user)
        l=len(s)
        context = super(PROFILE,self).get_context_data(**kwargs)
        context.update({"p":p,"l":l,"s":s})
        return context
    

class STORY(FormMixin,ListView):

    template_name="story.html"

    model=story

    ordering='-created_at'
  
    form_class=SEARCH

    paginate_by=7

    def get_queryset(self):
            qs=super().get_queryset()

            if 'search' in self.request.GET:
                f=SEARCH(self.request.GET)

                if f.is_valid():
                    cd=f.cleaned_data['search']

                    return qs.filter(Q(title__icontains=cd)|Q(caption__icontains=cd)|Q(user__username__icontains=cd))

            else:

                return qs


      
    




class HIS_PROFILE(ListView): 

    model=story

    #OR
    #queryset=story.objects

    template_name="his_profile.html"

    paginate_by=7



    def get_queryset(self):
        user=User.objects.get(username=self.kwargs['user'])
        qs=super().get_queryset()
        return qs.filter(user=user).order_by('-created_at')

    

    def get_context_data(self, **kwargs):
        #if self.request.method=='GET' and self.kwargs['search']:
         #   story.objects.filter(Q())

        #else:
        user=User.objects.get(username=self.kwargs['user'])
        p=personal_information.objects.filter(person=user)[0] if personal_information.objects.filter(person=user) else ""
        s=story.objects.filter(user=user)
        l=len(s)
        context = super(HIS_PROFILE,self).get_context_data(**kwargs)
        context.update({"u" : user,"p":p,"l":l})
        return context
    
    
   





    


