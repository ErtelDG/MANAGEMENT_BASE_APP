from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
#from datetime import datetime
from .models import Task
#from .views import index_kanban_board
from django.utils import timezone

class IndexKanbanBoardViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            prio='Low',
            member_type='Frontend',                            assigned=self.user,
            status='ToDo',
            created_at=timezone.now(),
            updated_at = timezone.now(),
        )
      
    
    def test_index_kanban_board_view(self):
        response = self.client.get('/management/kanban_board/')
        self.assertEqual(response.status_code, 200)
        
    def test_create_new_task(self):
        response = self.client.get('/management/kanban_board/add-task/')
        self.assertEqual(response.status_code, 200)
   
    def test_new_task_successfully(self):
        data = {
            'newTaskTitle': 'Test Task',
            'newTaskDescription': 'This is a test task.',
            'newTaskPrio': 'Low',
            'newMemberType': 'Frontend',
            'newTaskAssigned': self.user.pk,
            'newTaskStatus': 'ToDo',
        }
        response = self.client.post('/management/kanban_board/add-task/add-task-successfully/', data)
    
    def test_new_task_successfully_view(self):
        response = self.client.post('add-task/add-task-successfully',)
        
    def test_edit_task_view(self):
        data = {
            'newTaskTitle': 'EDIT Test Task',
            'newTaskDescription': 'EDIT This is a test task.',
            'newTaskPrio': 'Med',
            'newMemberType': 'Backend',
            'newTaskAssigned': self.user.pk,
            'newTaskStatus': 'Waiting',
        }
        response = self.client.post('edit_task', data, kwargs={'task_id': self.task.id})
    
    def test_edit_task_successfully_view(self):
        response = self.client.post('edit-task/<int:task_id>/edit-task-successfully', kwargs={'task_id': self.task.id})
    
    def test_delete_task_view(self):
        response = self.client.post('delete-task/<int:task_id>', kwargs={'task_id': self.task.id})
    
    def test_delete_task_successfully_view(self):
        response = self.client.post('delete-task/<int:task_id>/delete-task-successfully', kwargs={'task_id': self.task.id})