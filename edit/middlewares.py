from django.shortcuts import redirect

from django.contrib import messages

l=[
    '/home/','/login','/register','/admin/','/reset/done/','/confirm/done/','/reset/password'
]

class loginrequired:

    
    def __init__(self, get_response):
        self.get_response = get_response    

    def __call__(self, request):
        
        if not request.user.is_authenticated and request.path   not in l and 'confirm' not in str(request.path): 
           messages.error(request,"you should login first","login")
           return redirect('login')


        response = self.get_response(request)
        return response
