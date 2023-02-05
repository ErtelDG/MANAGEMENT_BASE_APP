from django.contrib import admin
# Import models for show on the admin side
from .models import Task

# Register imported models:
admin.site.register(Task)
