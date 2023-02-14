from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Task
from rest_framework import serializers
 

class TasksSerializer(serializers.HyperlinkedModelSerializer):
    assigned = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
  
    class Meta:
        model = Task
        fields = ['id','title', 'description', 'prio', 'member_type','status', 'assigned', 'created_at', 'updated_at', 'was_published_recently']