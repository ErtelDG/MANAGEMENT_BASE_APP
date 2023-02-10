from django.shortcuts import render

from django.template import loader

from kanban_board.models import Task

def index_kanban_board(request):
    template = loader.get_template('kanban_board/kanban_board_template.html')
    my_database = Task.objects.all()
    your_variable =['Hallo Noob','Hallo Noob2','Hallo Noob3']   
    
    return render(request, 'kanban_board/kanban_board_template.html',  {'WERT1':your_variable, 'DATABASE':my_database})
