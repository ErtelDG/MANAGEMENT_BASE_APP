from django.shortcuts import render

def index_kanban_board(request):
    return render(request, 'templates/kanban_board/kanban_board_template.html')
