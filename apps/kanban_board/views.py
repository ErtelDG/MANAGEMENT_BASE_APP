# It imports the render function from the django.shortcuts module, the User model from the
# django.contrib.auth.models module, the datetime module, the Task model from the kanban_board.models
# module, and the timezone module from the django.utils module.
from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import datetime
from kanban_board.models import Task, Subtask
from django.utils import timezone
from rest_framework import viewsets
from rest_framework import permissions
from kanban_board.serializers import TasksSerializer
from django.http import HttpResponse
from django.core import serializers
from rest_framework.decorators import api_view


"""
It takes a request, checks if it's a GET request, if it is, it gets all the tasks from the database
and returns them to the template.

:param request: The request object is a Python object that contains information about the current
HTTP request
:return: the rendered template.
"""
def index_kanban_board(request):
    if request.method == 'GET':
        toDo = Task.objects.filter(status="ToDo")
        working = Task.objects.filter(status="Working")
        waiting = Task.objects.filter(status="Waiting")
        done = Task.objects.filter(status="Done")
        userList = User.objects.all()
        return render(request, 'kanban_board/kanban_board_template.html', {'users': userList, 'toDos':toDo, 'workings':working, 'waitings':waiting, 'dones':done})
    return render(request, 'kanban_board/kanban_board_template.html',{'WERT1':'NO VALUE REQUEST'})



"""
It takes a request, gets all the users in the database, and renders the create_task.html page with
the list of users.

:param request: The request object is a standard Django object that contains metadata about the
request sent to the server
:return: The userList is being returned.
"""
def create_new_task(request):
    userList = User.objects.all()
    return render(request, 'kanban_board/create_task.html', {'users': userList})



"""
It creates a new task with the given parameters.

:param request: The request object is a Python object that contains all the information about the
request that was sent to the server
:return: a render of the create_succsessfully.html page.
"""
def new_task_successfully(request):
    if request.method == 'POST':
        Task.objects.create(
            title = request.POST["newTaskTitle"],
            description=request.POST["newTaskDescription"],
            prio = request.POST["newTaskPrio"],
            member_type=request.POST["newMemberType"],
            assigned=User.objects.get(pk=request.POST["newTaskAssigned"]),
            status=request.POST["newTaskStatus"],
            created_at = timezone.now(),
            updated_at = timezone.now(),
        )
    return render(request, 'kanban_board/create_succsessfully.html')



"""
It takes the task_id from the url, gets the task from the database, gets the user from the database,
and renders the edit_task.html page with the task and user information.

:param request: The request object is an HttpRequest object. It contains metadata about the request,
including the HTTP method
:param task_id: the id of the task that is being edited
:return: The selectedTask object is being returned.
"""
def edit_task(request, task_id):
    userList = User.objects.all()
    id = task_id
    selectedTask = Task.objects.get(pk=id)    
    user = User.objects.get(pk=selectedTask.assigned_id)
    subtask = Subtask.objects.filter(task_id=id)
    return render(request, 'kanban_board/edit_task.html', {'editTask':selectedTask, 'users': userList, 'currentUser': user, 'subtasks':subtask})



"""
It takes the task_id from the url, gets the task from the database, and then updates the task with
the new values from the form.

:param request: The request object is a Python object that contains all the information about the
request that was sent to the server
:param task_id: The id of the task you want to edit
:return: a render of the edit_succsessfully.html page.
"""
def edit_task_successfully(request, task_id):
    if request.method == 'POST':
        editTask = Task.objects.get(id=task_id)
        editTask.title =request.POST.get('editTitle')
        editTask.description = request.POST.get('editDescription')
        editTask.prio=request.POST.get('editPrio')
        editTask.member_type=request.POST.get('editType')
        #editTask.assigned=User.objects.get(pk=request.POST('editAssigned')),
        editTask.status=request.POST.get('editStatus')
        editTask.updated_at = datetime.now()
        editTask.save()
    return render(request, 'kanban_board/edit_succsessfully.html')



    """
    It takes a request and a task_id, gets the task with the given id, gets the user assigned to that
    task, and renders the delete_task.html page with the task and user.
    
    :param request: The request object is a Django object that contains metadata about the request sent
    to the server
    :param task_id: the id of the task that is being deleted
    :return: The delete_task view is returning the delete_task.html template, which is a form that
    allows the user to delete a task.
    """
def delete_task(request, task_id):
    userList = User.objects.all()
    id = task_id
    selectedTask = Task.objects.get(pk=id)    
    user = User.objects.get(pk=selectedTask.assigned_id)
    return render(request, 'kanban_board/delete_task.html', {'deleteTask':selectedTask, 'users': userList, 'currentUser': user})



"""
It deletes a task from the database.

:param request: The request object is a Django object that contains metadata about the request sent
to the server
:param task_id: The id of the task that you want to delete
:return: The render function is being returned.
"""
def delete_task_successfully(request, task_id):
    if request.method == 'POST':
        deleteTask = Task.objects.get(id=task_id)
        deleteTask.delete()
    return render(request, 'kanban_board/delete_succsessfully.html')


class TasksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('-status')
    serializer_class = TasksSerializer
    permission_classes = []#permissions.IsAuthenticated
   
    def create(self, request):
        if request.method == 'POST':
            requestValue=self.request.data       
            task = Task.objects.create(
                title = requestValue['newTaskTitle'] ,
                description=requestValue['newTaskDescription'],
                prio = requestValue['newTaskPrio'],
                member_type=requestValue['newMemberType'],
                assigned=User.objects.get(pk=requestValue["newTaskAssigned"]),
                status=requestValue['newTaskStatus'],
                created_at = timezone.now(),
                updated_at = timezone.now(),
            )
            serialized_obj = serializers.serialize('json', [task, ]) 
            return HttpResponse(serialized_obj, content_type='application/json')