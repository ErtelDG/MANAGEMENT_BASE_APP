# Importing the render function from the django.shortcuts module.
from django.shortcuts import render
from django.contrib.auth.models import User


"""
It takes a request object, and returns a rendered template

:param request: The request is an HttpRequest object
:return: The render function is being returned.
"""
def index_accounts(request):
    return render(request, 'accounts/accounts_template.html')


"""
It creates a user object with the information provided by the user in the registration form

:param request: The request is an HttpRequest object
:return: The render function is being returned.
"""
def registered(request):
    
    if request.method == "POST":
       
        user = User.objects.create_user(
            username=request.POST.get("username"),
            first_name=request.POST.get("firstname"),
            last_name=request.POST.get("lastname"),
            email=request.POST.get("useremail"),
            password=request.POST.get("userpassword"),
        )
    return render(request, 'registration/registered.html',)
