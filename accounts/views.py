from django.shortcuts import render,redirect

# Create your views here.
from .forms import register,PasswordResetForm

from django.urls import reverse_lazy

from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth.views import LogoutView,LoginView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

from django.core.mail import send_mail

from django.template.loader import render_to_string

from django.utils.http import urlsafe_base64_encode

from django.contrib.auth.tokens import default_token_generator

from django.utils.encoding import force_bytes


def REGISTER(request):
    if request.method=='GET':
        return render (request,'registration/register.html',{'form':register()})
    elif request.method=="POST":
        f=register(request.POST)
        print(f)
        if f.is_valid():
           first_name=f.cleaned_data['first_name']
           last_name=f.cleaned_data['last_name']
           username=f.cleaned_data['username']
           email=f.cleaned_data['email']
           password=f.cleaned_data['password']
           password2=f.cleaned_data['password2']

           if password==password2:
                if User.objects.filter(username=username).exists():
                   messages.error(request,'that username is taken')
                   return render (request,'registration/register.html',{'form':f})
                elif User.objects.filter(email=email).exists():
                   messages.error(request,'that email is being used')
                   return render (request,'registration/register.html',{'form':f})
                else:
                    user=User.objects.create_user(username=username,
                    email=email,
                    password=password,
                    first_name=first_name,last_name=last_name)
                    user.save()
                    messages.success(request,'you are now registered and can log in')
                    return render (request,'registration/register.html',{'form':f})
           else:
                messages.error(request,"Password don't match")
                return render (request,'registration/register.html',{'form':f})
        else:
            return render (request,'registration/register.html',{'form':f})
    else:
        pass



class LOGIN(LoginView):

    template_name="registration/login.html"


class LOGOUT(LogoutView):

	template_name = 'registration/logout.html'

def password_reset_form (request):
    if request.method =='GET':
        return render (request,'registration/password_reset_form.html',{'form':PasswordResetForm()})
    elif request.method=='POST':
        f=PasswordResetForm(request.POST)
        if f.is_valid():
            data=f.cleaned_data['email']
            user=User.objects.filter(email=data)
            if user.exists():
                subject="Password Reset Requested"

                email_template_name = 'registration/password_reset_email.html'
                user=User.objects.get(email=data)

                context = {
					"email":user.email,
					'domain':'127.0.0.1',
					'site_name': 'radiobeech',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
                email = render_to_string(email_template_name,context)
                send_mail(subject,email,'Radio Beech',[user.email,],fail_silently=False)
                return redirect('password_reset_done')
	
		
				
            else:
                messages.error(request,"the email doesn't exist")
                return render (request,'registration/password_reset_form.html',{'form':f})
        else:
            messages.error(request,"enter a correct email")
            return render (request,'registration/password_reset_form.html',{'form':f})
            

class PASSWORD_RESET_DONE(PasswordResetDoneView):
	template_name = 'registration/password_reset_done.html'

class PASSWORD_RESET_CONFIRM(PasswordResetConfirmView):
	template_name = 'registration/password_reset_confirm.html'
	success_url = reverse_lazy('password_reset_complete')

class PASSWORD_RESET_COMPLETE(PasswordResetCompleteView):
	template_name = 'registration/password_reset_complete.html'

   
	








































    









			   
    
	    