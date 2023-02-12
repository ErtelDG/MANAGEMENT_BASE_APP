from django.shortcuts import render
from django.contrib.auth.models import User
from django.template import loader
from datetime import datetime
from kanban_board.models import Task

def index_kanban_board(request):
    
    if request.method == 'GET':
        toDo = Task.objects.filter(status="ToDo")
        working = Task.objects.filter(status="Working")
        waiting = Task.objects.filter(status="Waiting")
        done = Task.objects.filter(status="Done")
        print('PRINTING FOR SEE toDo',toDo)
        print('PRINTING FOR SEE working',working)
        print('PRINTING FOR SEE waiting',waiting)
        print('PRINTING FOR SEE done',done)
        userList = User.objects.all()
        return render(request, 'kanban_board/kanban_board_template.html', {'users': userList, 'toDos':toDo, 'workings':working, 'waitings':waiting, 'dones':done})
    return render(request, 'kanban_board/kanban_board_template.html',{'WERT1':'NO VALUE REQUEST'})



def create_new_task(request):
    userList = User.objects.all()
    return render(request, 'kanban_board/create_task.html', {'users': userList})

def new_task_successfully(request):

    if request.method == 'POST':
        
        Task.objects.create(
            title = request.POST["newTaskTitle"],
            description=request.POST["newTaskDescription"],
            prio = request.POST["newTaskPrio"],
            member_type=request.POST["newMemberType"],
            assigned=User.objects.get(pk=request.POST["newTaskAssigned"]),
            status=request.POST["newTaskStatus"],
            created_at = datetime.now(),
            updated_at = datetime.now(),
        )

    return render(request, 'kanban_board/create_succsessfully.html')
