"""MANAGEMENT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# HIER APPS EINBINDEN, ERKLÄRUNG ARGUMENTE: https://docs.djangoproject.com/en/4.1/intro/tutorial01/ :
urlpatterns = [
    # ADMIN EINBINDEN:
    path('admin/', admin.site.urls, name="admin"),
    # MANAGEMENT_APP EINBENDEN ÜBER DREI URLS ABRUFBAR:
    path('management_app/', include('management_app.urls'), name="management_app"),
    path('', include('management_app.urls')),
    path('index/', include('management_app.urls')),
]
