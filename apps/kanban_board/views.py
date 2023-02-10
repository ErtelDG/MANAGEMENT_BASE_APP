from django.shortcuts import render
from django.contrib.auth.models import User
from django.template import loader
from datetime import datetime
from kanban_board.models import Task

def index_kanban_board(request):
    
   
    
    if request.method == 'POST':
        userList = User.objects.all()
             
        print(request.POST.get("newTaskTitle"))        
        print(request.POST.get("newTaskDescription"))        
        print(request.POST.get("newTaskPrio"))        
        print(request.POST.get("newMemberType"))        
        print(request.POST.get("newTaskAssigned"))        
        print(request.POST.get("newTaskStatus"))
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
        userList = User.objects.all()
        return render(request, 'kanban_board/kanban_board_template.html', {'users': userList})
    return render(request, 'kanban_board/kanban_board_template.html',{'WERT1':'NO VALUE REQUEST'})



def create_new_task(request):
    return render(request, 'kanban_board/kanban_board_template.html',  {'WERT1':'HARD CODE VALUE1', 'DATABASE':'HARD CODE DATABASE VALUE1'})
