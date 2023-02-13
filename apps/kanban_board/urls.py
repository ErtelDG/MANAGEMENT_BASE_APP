from django.urls import path, re_path

from . import views


# HIER PATH VON DER MANAGEMENT APP:
urlpatterns = [
    path('', views.index_kanban_board, name='index_kanban_board'),
    path('add-task/', views.create_new_task, name='create_new_task'),
    path('add-task/add-task-successfully/', views.new_task_successfully, name='new_task_successfully'),
    path('edit-task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('edit-task/<int:task_id>/edit-task-successfully/', views.edit_task_successfully, name='edit_task_successfully'),
    path('delete-task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('delete-task/<int:task_id>/delete-task-successfully/', views.delete_task_successfully, name='delete_task_successfully'),
]