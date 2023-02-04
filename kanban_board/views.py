from django.http import HttpResponse

def index_kanban_board(request):
    return HttpResponse("KANBAN_BOARD_TEMPLATE")
