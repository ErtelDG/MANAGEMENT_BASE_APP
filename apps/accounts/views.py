from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def index_accounts(request):
    return render(request, 'accounts/accounts_template.html')

# signUp view
def registered(request):
    
    if request.method == "POST":
        print(request.POST.get("username")),
        print(request.POST.get("firstname")),
        print(request.POST.get("lastname")),
        print(request.POST.get("useremail")),
        print(request.POST.get("userpassword")),
       
        user = User.objects.create_user(
            username=request.POST.get("username"),
            first_name=request.POST.get("firstname"),
            last_name=request.POST.get("lastname"),
            email=request.POST.get("useremail"),
            password=request.POST.get("userpassword"),
        )
    return render(request, 'registration/registered.html',)
