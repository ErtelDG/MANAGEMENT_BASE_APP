from django.shortcuts import render

def index_accounts(request):
    return render(request, 'accounts/accounts_template.html')
