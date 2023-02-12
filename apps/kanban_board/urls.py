from django.urls import path

from . import views


# HIER PATH VON DER MANAGEMENT APP:
urlpatterns = [
    path('', views.index_kanban_board, name='index_kanban_board'),
    path('add-task/', views.create_new_task, name='create_new_task'),
    path('add-task/add-task-successfully/', views.new_task_successfully, name='new_task_successfully'),
]