from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Student(models.Model):

  stu           = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

  type          = models.CharField(max_length=10, default='Student')
  student_id    = models.CharField(max_length=7, default='')
  major         = models.CharField(max_length=30, default='')
  hours         = models.PositiveSmallIntegerField(default=0)
  in_internship = models.BooleanField(default=False)
  in_gp         = models.BooleanField(verbose_name='in graduation-project',default=False)
  
  
  def __str__(self) -> str:
    return str(self.stu)







################################################################
######################### Internship ###########################
################################################################

class CompanyInternship(models.Model):

  # Student
  student = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

  # Company Info
  company = models.CharField(max_length=80, verbose_name="Company Name")
  address = models.CharField(max_length=80,)
  start   = models.DateField(verbose_name="starting Date")
  end     = models.DateField(verbose_name="Ending Date")

  # Superviser Info
  name      = models.CharField(max_length=80, verbose_name="Superviser Name")
  email     = models.EmailField(max_length=80, verbose_name="Superviser Email")

  # Technical Info
  description_of_tasks  = models.CharField(max_length=450,)
  technologies          = models.CharField(max_length=450,)


  def __str__(self):
    return str(self.student.first_name ) + " Company Internship"






class CourseInternship(models.Model):

  # Student
  stu = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  
  # Course Info
  course      = models.CharField(max_length=80, verbose_name="Course Name")
  hour        = models.PositiveSmallIntegerField()
  provider    = models.CharField(max_length=80, verbose_name="Course Provider")
  certificate = models.FileField(upload_to='files/', null=True)

  def __str__(self):
    return str(self.stu) + " Course"






class WeeklyFollowing(models.Model):
  
  # Student
  stu_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  stu_name = models.CharField(max_length=64)

  # Task Info
  task         = models.CharField(max_length=50)
  hours        = models.PositiveSmallIntegerField()
  technologies = models.TextField(max_length=450)
  evaluation   = models.CharField(max_length=16)