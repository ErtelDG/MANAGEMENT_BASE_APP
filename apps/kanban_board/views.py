from django.shortcuts import render

from django.template import loader

from kanban_board.models import Task

def index_kanban_board(request):
    if request.method == 'POST':
        my_database = Task.objects.all()
        your_variable =['Hallo Noob','Hallo Noob2','Hallo Noob3']   
        return render(request, 'kanban_board/kanban_board_template.html',{'WERT1':your_variable, 'DATABASE':my_database, 'responseInfoAddTaskCreated': 'New task successfully',})
    
    if request.method == 'GET':
        return render(request, 'kanban_board/kanban_board_template.html')
    return render(request, 'kanban_board/kanban_board_template.html',{'WERT1':'NO VALUE REQUESTT', 'DATABASE':'NO VALUE REQUEST DATABASE'})



def create_new_task(request):
    return render(request, 'kanban_board/kanban_board_template.html',  {'WERT1':'HARD CODE VALUE1', 'DATABASE':'HARD CODE DATABASE VALUE1'})
