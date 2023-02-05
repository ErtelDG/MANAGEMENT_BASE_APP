from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import datetime

PRIO_CHOICES=[
  ('1','Low'),
  ('2','Med'),
  ('3','Urg'),
]


MEMBER_TYPE_CHOICES=[
  ('1','Frontend'),
  ('2','Backend'),
  ('3','UI/UX Design'),
  ('4','Product Owner'),
  ('5','Srum Master'),
  ('6','Testing'),
]


STATUS_CHOICES=[
  ('1','ToDo'),
  ('2','Working'),
  ('3','Waiting'),
  ('4','Done'),
]


class Task(models.Model):
    title = models.CharField(max_length=200, default="No Title")
    description = models.CharField(max_length=400, default="No description")
    prio = models.CharField(max_length=1, choices=PRIO_CHOICES, default=1)
    member_type = models.CharField(max_length=1, choices=MEMBER_TYPE_CHOICES, default=1)
    assigned = models.ForeignKey(User, on_delete=models.PROTECT)
    status=models.CharField(max_length=1, choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #It’s important to add __str__() methods to your models, not only for your own convenience when dealing with the interactive prompt, but also because objects’ representations are used throughout Django’s automatically-generated admin.
    #def __str__(self):
    #    return self.choice_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)