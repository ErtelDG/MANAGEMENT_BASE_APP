from django.urls import path

from . import views


# HIER PATH VON DER ACCOUNTS APP:
urlpatterns = [
    path('', views.index_accounts, name='index_accounts'),
]