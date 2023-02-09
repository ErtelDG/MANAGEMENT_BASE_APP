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
from django.views.generic.base import TemplateView

# HIER APPS EINBINDEN, ERKLÄRUNG ARGUMENTE: https://docs.djangoproject.com/en/4.1/intro/tutorial01/ :
urlpatterns = [
    #HOME START Verzeichnis EINBINDEN:
    path('', TemplateView.as_view(template_name='home/home.html'), name='home'),
    path('home/', TemplateView.as_view(template_name='home/home.html'), name='home'),
    # ADMIN Verzeichnis EINBINDEN:
    path('admin/', admin.site.urls, name="admin"),
    # ACCOUNTS Verzeichnis EINBINDEN:
    path("accounts/", include("accounts.urls")),
        # MANAGEMENT Verzeichnis APP EINBINDEN:
    path('management/', TemplateView.as_view(template_name='home/home.html'), name='home'),
    # KANBAN_BOARD Verzeichnis EINBINDEN:
    path('management/kanban_board/', include('apps.kanban_board.urls'), name='kanban_board_side'),
    #Include django_browser_reload URL in your root url.py, which takes care of automatic page and css refreshes in the development mode.:
    path("__reload__/", include("django_browser_reload.urls")),
    #If you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views. Add the following to your root urls.py file.
    path('api-auth/', include('rest_framework.urls')),
]
