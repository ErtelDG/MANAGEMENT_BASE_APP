# It imports the User model from Django's auth app.
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import datetime

# A list of tuples.
PRIO_CHOICES=[
  ('Low','Low'),
  ('Medium','Medium'),
  ('Urgent','Urgent'),
]


# A list of tuples.
MEMBER_TYPE_CHOICES=[
  ('Frontend','Frontend'),
  ('Backend','Backend'),
  ('UI/UX Design','UI/UX Design'),
  ('Product Owner','Product Owner'),
  ('Srum Master','Srum Master'),
  ('Testing','Testing'),
]


# A list of tuples.
STATUS_CHOICES=[
  ('ToDo','ToDo'),
  ('Working','Working'),
  ('Waiting','Waiting'),
  ('Done','Done'),
]


# It creates a model for the database.
class Task(models.Model):
    title = models.CharField(max_length=200, default="No Title")
    description = models.CharField(max_length=400, default="No description")
    prio = models.CharField(max_length=20, choices=PRIO_CHOICES, default='Low')
    member_type = models.CharField(max_length=20, choices=MEMBER_TYPE_CHOICES, default='Frontend')
    assigned = models.ForeignKey(User, on_delete=models.PROTECT)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='ToDo')
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')
    
    #It’s important to add __str__() methods to your models, not only for your own convenience when dealing with the interactive prompt, but also because objects’ representations are used throughout Django’s automatically-generated admin.
    #def __str__(self):
    #    return self.choice_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)