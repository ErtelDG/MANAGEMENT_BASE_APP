from django.urls import path, include

from . import views
from apps.kanban_board import views as  index_kanban_board


# HIER PATH VON DER MANAGEMENT APP:
urlpatterns = [
    path('', views.index_base, name='index_base'),
    path('/kanban_board/', include('apps.kanban_board.urls'), name='kanban_board_side')
]