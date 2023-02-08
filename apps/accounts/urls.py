from django.urls import path,include
from . import views
from django.views.generic.base import TemplateView

# HIER PATH VON DER ACCOUNTS APP:
urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path("signup_user/", TemplateView.as_view(template_name='registration/signup.html'), name="signup_user"),
    path('registered/', views.registered, name="registered"),
    
]