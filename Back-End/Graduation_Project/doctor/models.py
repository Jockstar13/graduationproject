from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Doctor(models.Model):

  per = (
    ('doc', 'Doctor'),
    ('sec', 'Secretary'),
    ('doc&head', 'Doctor and Head'),
  )

  doc                           = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  
  job_number                    = models.PositiveIntegerField(default=0)
  department                    = models.CharField(max_length=30, default='')
  permission                    = models.CharField(max_length=15, choices=per, default='doc')
  no_stu_in_internship          = models.PositiveSmallIntegerField(default=0)
  no_stu_in_grasduation_project = models.PositiveSmallIntegerField(default=0)

  
  def __str__(self):
    return str(self.doc) + ' ' + str(self.permission)






################################################################
######################## Notification ##########################
################################################################
class DoctorNotification(models.Model):
  
  doctor    = models.ForeignKey(User, on_delete=models.CASCADE)
  url_name  = models.CharField(max_length=24, null=True)
  query_pk  = models.CharField(max_length=32, null=True)
  subject   = models.CharField(max_length=56)
  message   = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)
  is_read   = models.BooleanField(default=False)
  
  def __str__(self):
    return str(self.doctor) + ' -- ' + self.subject