from django.db import models

# Create your models here.



class Doctor(models.Model):

  per = (
    ('doc', 'Doctor'),
    ('sec', 'Secretary'),
    ('doc&head', 'Doctor and Head'),
  )



  id                            = models.AutoField(primary_key=True)
  full_name                     = models.CharField(max_length=50, default='')
  username                      = models.CharField(max_length=8, default='')
  job_number                    = models.PositiveIntegerField(default=0)
  email                         = models.EmailField(max_length=100, default='')
  password                      = models.CharField(max_length=70, unique=True)
  department                    = models.CharField(max_length=30, default='')
  permission                    = models.CharField(max_length=15, choices=per, default='doc')
  no_stu_in_internship          = models.PositiveSmallIntegerField(default=0)
  no_stu_in_grasduation_project = models.PositiveSmallIntegerField(default=0)

  
  def __str__(self):
    return self.department