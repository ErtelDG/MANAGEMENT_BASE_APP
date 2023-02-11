from django.shortcuts import render
from django.contrib.auth.models import User
from django.template import loader
from datetime import datetime
from kanban_board.models import Task

def index_kanban_board(request):
    
   
    
    if request.method == 'POST':
        userList = User.objects.all()
      
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
                  
        your_variable =['Hallo Noob','Hallo Noob2','Hallo Noob3']   
        return render(request, 'kanban_board/kanban_board_template.html',{'WERT1':your_variable, 'responseInfoAddTaskCreated': 'New task successfully', 'users': userList})
    
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
    return render(request, 'kanban_board/kanban_board_template.html',  {'WERT1':'HARD CODE VALUE1', 'DATABASE':'HARD CODE DATABASE VALUE1'})
