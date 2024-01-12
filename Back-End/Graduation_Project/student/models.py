from django.db import models
from doctor.models import Doctor
from django.contrib.auth.models import User



# Create your models here.



class Student(models.Model):

  stu             = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  doc_superviser  = models.ForeignKey(Doctor, on_delete=models.PROTECT, null=True)

  student_id      = models.CharField(max_length=7, default='')
  major           = models.CharField(max_length=32, default='')
  hours           = models.PositiveSmallIntegerField(default=0)
  in_internship   = models.BooleanField(default=False)
  in_gp           = models.BooleanField(verbose_name='in graduation-project',default=False)
  
  
  def __str__(self) -> str:
    return str(self.stu)


  # def get_username(self):
  #   return (self.stu)




################################################################
##################### Graduation Project #######################
################################################################

class GraduationProject(models.Model):

  sems =(
    ('First', 'First'),
    ('Second', 'Second'),
    ('Summer', 'Summer'),
  )

  pro_type =(
    ('Application', 'Application'),
    ('Research', 'Research'),
  )


  # Student
  members    = models.ManyToManyField(User)

  # Main
  department = models.CharField(max_length=32)
  semester   = models.CharField(max_length=8)


  # Student Info
  # students_info = models.FileField(upload_to=r'Files/Graduation-Project/%Y/%B/', null=True)

  # Doctors Info
  superviser_1   = models.CharField(max_length=32, null=True)
  email_1        = models.CharField(max_length=32, null=True)
  superviser_2   = models.CharField(max_length=32, null=True)
  email_2        = models.CharField(max_length=32, null=True)


  # Project Info
  project_type = models.CharField(max_length=12)
  project_name = models.CharField(max_length=128)
  project_idea = models.TextField(max_length=720)
  project_goal = models.TextField(max_length=400)
  technologies = models.TextField(max_length=400)


  def __str__(self):
    return self.project_name



################################################################
####################### STUDENT RATING #########################
################################################################
class StudentRating(models.Model):
    
  stu_username   = models.OneToOneField(Student, on_delete=models.CASCADE, null=True)
  
  web_dev_rating      = models.FloatField()
  network_rating      = models.FloatField()
  security_rating     = models.FloatField()
  data_science_rating = models.FloatField()


  def __str__(self):
    return str(self.stu_username)




################################################################
##################### Recommended Project ######################
################################################################


class GraduationDetails(models.Model):

  # project           = models.OneToOneField(RecommendedProject, on_delete=models.CASCADE)
  overview       = models.TextField()

  first_subtitle   = models.CharField(max_length=64, null=True)
  first_paragraph  = models.TextField(null=True)

  second_subtitle  = models.CharField(max_length=64, null=True)
  second_paragraph = models.TextField(null=True)

  weekly_hours     = models.IntegerField(default=0.0)


  technologies_used = models.CharField(max_length=255)
  what_to_learn     = models.TextField()


  def __str__(self):
    return self.overview



class RecommendedProject(models.Model):

  title = models.CharField(max_length=255, )
  details = models.OneToOneField(GraduationDetails, on_delete=models.CASCADE, null=True)

  web_dev      = models.FloatField(default=0.0)
  network      = models.FloatField(default=0.0)
  security     = models.FloatField(default=0.0)
  data_science = models.FloatField(default=0.0)


  # description  = models.TextField(default='')
  # weekly_hours = models.IntegerField(default=0.0)
  # title_sub    = models.CharField(max_length=255,default='')

  def __str__(self):
    return str(self.title)





################################################################
####################### TIMELINE FILES #########################
################################################################
class TimlineFiles(models.Model):
  
  file = models.FileField(upload_to='GP/Timeline/%Y/%B/%A', null=True)

  def __str__(self):
    return self.file.name.split('/')[-1]



################################################################
########################## TIMELINE ############################
################################################################
class Timeline(models.Model):

  members          = models.ManyToManyField(User)
  team             = models.ForeignKey(GraduationProject, on_delete=models.CASCADE, null=True)
    
  important        = models.BooleanField(default=False)
  doc              = models.BooleanField(default=False)
  update           = models.BooleanField(default=False)
  final_release    = models.BooleanField(default=False)
  new_release      = models.BooleanField(default=False)
  research         = models.BooleanField(default=False)
  programming      = models.BooleanField(default=False)
  problem          = models.BooleanField(default=False)
  web              = models.BooleanField(default=False)
  mobile           = models.BooleanField(default=False)
  network          = models.BooleanField(default=False)
  cyber_security   = models.BooleanField(default=False)
  ai               = models.BooleanField(default=False)
  machine_learning = models.BooleanField(default=False)

  post             = models.TextField()
  files            = models.ManyToManyField(TimlineFiles)
  date             = models.DateTimeField(null=True)
  publisher        = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)



  def __str__(self):
    return f'{self.publisher} -- {self.date.date().day} - {self.date.time()}'







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

  # Acceptance
  doc_note    = models.TextField(max_length=450, null=True, default='There is no Notes')
  int_com_acc = models.BooleanField(verbose_name='internship acceptance',default=False)

  def __str__(self):
    return str(self.email) + " Company Internship"




class CourseInternship(models.Model):

  # Student
  stu         = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  s           = Student()
  
  # Course Info
  course      = models.CharField(max_length=80, verbose_name="Course Name")
  hour        = models.PositiveSmallIntegerField()
  provider    = models.CharField(max_length=80, verbose_name="Course Provider")
  certificate = models.FileField(upload_to=f'Internship/Courses/%Y/%B', null=True)

  # Acceptance
  doc_note    = models.TextField(max_length=450, null=True, default='There is no any note yet.')
  int_cor_acc = models.BooleanField(verbose_name='internship acceptance',default=False)



  def __str__(self):
    return str(self.stu) + " Course" + str(self.pk)







class WeeklyFollowing(models.Model):
  
  # Student
  stu_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

  # Week
  week = models.CharField(max_length=6, null=True)

  # Task Info
  task  = models.CharField(max_length=50)
  hour  = models.PositiveSmallIntegerField()
  sw_hw = models.TextField(max_length=650, null=True)

  def __str__(self):
    return str(self.stu_user) + str(self.week)
  







################################################################
######################## Notification ##########################
################################################################
class StudentNotification(models.Model):
  
  student   = models.ForeignKey(User, on_delete=models.CASCADE)
  url_name  = models.CharField(max_length=24, null=True)
  query_pk  = models.CharField(max_length=32, null=True)
  subject   = models.CharField(max_length=56)
  message   = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)
  is_read   = models.BooleanField(default=False)

  def __str__(self):
    return str(self.student) + ' -- ' + self.subject