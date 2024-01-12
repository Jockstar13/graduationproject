from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User

# Create your models here.


class Department(models.Model):


  depts = (
    ('Computer Science'               , 'Computer Science'),
    ('Computer Information Systems'   , 'Computer Information Systems'),
    ('Business Information Technology', 'Business Information Technology'),
    ('Data Science'                   , 'Data Science'),
    ('Cyber Security'                 , 'Cyber Security'),
    ('Artificial Intelligence'        , 'Artificial Intelligence'),
  )
  
  dept_name       = models.CharField(max_length=32, choices=depts)
  num_team_member = models.PositiveSmallIntegerField(default=4, verbose_name="Number of team's member")
  start           = models.DateField(editable=True, default='')
  end             = models.DateField(editable=True, default='')

  week            = models.PositiveIntegerField(default=1)



  def is_less_than_start(self):
    today_date = date.today()
    return self.start > today_date

  def is_greater_than_end(self):
    today_date = date.today()
    return self.end < today_date




  def __str__(self):
    return self.dept_name




################################################################
######################## Notification ##########################
################################################################
class DepartmentNotification(models.Model):
  
  department = models.ForeignKey(Department, on_delete=models.CASCADE)
  url_name   = models.CharField(max_length=24, null=True)
  query_pk   = models.CharField(max_length=32, null=True)
  subject    = models.CharField(max_length=56)
  message    = models.TextField()
  timestamp  = models.DateTimeField(auto_now_add=True)
  is_read    = models.BooleanField(default=False)
  
  def __str__(self):
    return str(self.department) + ' -- ' + self.subject