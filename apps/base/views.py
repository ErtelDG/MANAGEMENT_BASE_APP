from django.shortcuts import render

def index_accounts(request):
    return render(request, 'templates/base/accounts_template.html')

def index_base(request):
    return render(request, 'templates/base/base_template.html')
  