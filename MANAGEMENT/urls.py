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
from rest_framework import routers
from django.conf.urls.static import static
from apps.kanban_board.views import TasksViewSet
from MANAGEMENT import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
router = routers.DefaultRouter()
router.register(r'tasks', TasksViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
   
    # A way to create a home page.
    path('', TemplateView.as_view(template_name='home/home.html'), name='home'),
    path('home/', TemplateView.as_view(template_name='home/home.html'), name='home'),
    
    # A way to create a home page.
    path('admin/', admin.site.urls, name="admin"),
    
    # Including the urls.py file from the accounts app.
    path("accounts/", include("accounts.urls")),
       
    
    # A way to create a home page.
    path('management/', TemplateView.as_view(template_name='home/home.html'), name='home'),
    
    
    # Including the urls.py file from the kanban_board app.
    path('management/kanban_board/', include('apps.kanban_board.urls'), name='kanban_board_side'),
    
    #Include django_browser_reload URL in your root url.py, which takes care of automatic page and css refreshes in the development mode.:
    path("__reload__/", include("django_browser_reload.urls")),
    
    #If you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views. Add the following to your root urls.py file.
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
