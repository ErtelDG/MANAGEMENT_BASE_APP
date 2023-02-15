# Importing the render function from the django.shortcuts module.
from django.shortcuts import render
from django.contrib.auth.models import User
import re


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
        getNewUsername = request.POST.get("username")
        getFirstName=request.POST.get("firstname")
        getLastName=request.POST.get("lastname")
        getEmail=request.POST.get("useremail")
        getPassword=request.POST.get("userpassword")
        
        lengthNewUsername = len(getNewUsername)
        lengthFirstName = len(getFirstName)
        lengthLastName = len(getLastName)
        lengthPassword = len(getPassword)
        
        if User.objects.filter(username=getNewUsername).exists():
            return render(request, 'registration/signup.html',{'mistakeUsernameExists': 'User exists. Try another username.', 'inputEmail':getEmail,'inputLastName':getLastName,'inputFirstName':getFirstName, 'inputUsername':getNewUsername, 'inputPassword':getPassword})
        elif  lengthNewUsername < 5 or lengthNewUsername > 20:
            return render(request, 'registration/signup.html',{'mistakeUsername': 'Required. 5-20 characters or fewer. Letters only.', 'inputEmail':getEmail,'inputLastName':getLastName,'inputFirstName':getFirstName, 'inputUsername':getNewUsername, 'inputPassword':getPassword})
        elif lengthFirstName < 2 or lengthFirstName > 20:
            return render(request, 'registration/signup.html',{'mistakeFirstName': 'Required. 2-20 characters or fewer. Letters only.','inputEmail':getEmail,'inputLastName':getLastName,'inputFirstName':getFirstName, 'inputUsername':getNewUsername, 'inputPassword':getPassword})
        elif lengthLastName < 2 or lengthLastName > 20:
            return render(request, 'registration/signup.html',{'mistakeLastName': 'Required. 2-20 characters or fewer. Letters only.','inputEmail':getEmail,'inputLastName':getLastName,'inputFirstName':getFirstName, 'inputUsername':getNewUsername, 'inputPassword':getPassword})
        elif not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", getEmail):
            return render(request, 'registration/signup.html',{'mistakeEmail': 'Enter a valid email!','inputEmail':getEmail,'inputLastName':getLastName,'inputFirstName':getFirstName, 'inputUsername':getNewUsername, 'inputPassword':getPassword})
        elif lengthPassword < 8:
            return render(request, 'registration/signup.html',{'mistakePassword': 'Your password must contain at least 8 characters.','inputEmail':getEmail,'inputLastName':getLastName,'inputFirstName':getFirstName, 'inputUsername':getNewUsername, 'inputPassword':getPassword})
        else:
            user = User.objects.create_user(
                username=getNewUsername,
                first_name=getFirstName,
                last_name=getLastName,
                email=getEmail,
                password=getPassword,
            )
    return render(request, 'registration/registered.html',)
