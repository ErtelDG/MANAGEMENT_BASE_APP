# It imports the TestCase class from the django.test module, the Client class from the django.test
# module, the User class from the django.contrib.auth.models module, the Task class from the .models
# module and the timezone class from the django.utils module.
from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Task
from django.utils import timezone

class IndexKanbanBoardViewTest(TestCase):


    """
    The setUp function is a function that is run before each test is executed
    """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            prio='Low',
            member_type='Frontend',
            assigned=self.user,
            status='ToDo',
            created_at=timezone.now(),
            updated_at = timezone.now(),
        )
      
    
    """
    > The test_index_kanban_board_view function tests that the index view of the KanbanBoard app returns
    a 200 status code
    """
    def test_index_kanban_board_view(self):
        response = self.client.get('/management/kanban_board/')
        self.assertEqual(response.status_code, 200)
    
      
    """
    > The test_create_new_task function tests that the add-task page is accessible
    """
    def test_create_new_task(self):
        response = self.client.get('/management/kanban_board/add-task/')
        self.assertEqual(response.status_code, 200)
 
   
    """
    The function tests if a new task can be created successfully
    """
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
    
    
    """
    It tests the view for the add-task-successfully page.
    """
    def test_new_task_successfully_view(self):
        response = self.client.post('add-task/add-task-successfully',)
    
        
    """
    A test function that tests the edit_task view.
    """
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
    
    
    """
    A test function that tests the edit-task-successfully view.
    """
    def test_edit_task_successfully_view(self):
        response = self.client.post('edit-task/<int:task_id>/edit-task-successfully', kwargs={'task_id': self.task.id})
    
    
    """
    The function `test_delete_task_view` is a test function that tests the
    `delete-task/<int:task_id>` view
    """
    def test_delete_task_view(self):
        response = self.client.post('delete-task/<int:task_id>', kwargs={'task_id': self.task.id})
    
    
    """
    It deletes the task.
    """
    def test_delete_task_successfully_view(self):
        response = self.client.post('delete-task/<int:task_id>/delete-task-successfully', kwargs={'task_id': self.task.id})