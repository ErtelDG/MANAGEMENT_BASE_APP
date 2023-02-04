from django.urls import path

from . import views

# HIER PATH VON DER MANAGEMENT APP:
urlpatterns = [
    path('', views.index, name='index'),
]