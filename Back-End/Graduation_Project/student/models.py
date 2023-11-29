from django.db import models

# Create your models here.



class Student(models.Model):
  
  id            = models.AutoField(primary_key=True)
  full_name     = models.CharField(max_length=50, default='')
  username      = models.CharField(max_length=9, default='')
  student_id    = models.CharField(max_length=6, default='')
  email         = models.EmailField(max_length=100, default='')
  password      = models.CharField(max_length=70, default='')
  gender        = models.CharField(max_length=6, default='')
  major         = models.CharField(max_length=30, default='')
  hours         = models.PositiveSmallIntegerField(default=0)
  in_internship = models.BooleanField(default=False)
  in_gp         = models.BooleanField(verbose_name='in graduation-project',default=False)
  
  
  def __str__(self):
    return self.major