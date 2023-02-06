from django.shortcuts import render

def index_accounts(request):
    return render(request, 'templates/accounts/accounts_template.html')
