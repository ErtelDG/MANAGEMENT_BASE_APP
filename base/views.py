from django.http import HttpResponse
from django.urls import path, include

def index_base(request):
    return HttpResponse("BASETEMPLATE")
  