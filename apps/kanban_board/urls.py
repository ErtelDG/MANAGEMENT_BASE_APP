from django.urls import path

from . import views


# HIER PATH VON DER MANAGEMENT APP:
urlpatterns = [
    path('', views.index_kanban_board, name='index_kanban_board'),
]