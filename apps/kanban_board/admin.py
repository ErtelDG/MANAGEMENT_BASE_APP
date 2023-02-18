from django.contrib import admin
# Import models for show on the admin side
from .models import Task, Subtask

# Register imported models:
admin.site.register(Task)
admin.site.register(Subtask)
