from django.db import models

# Create your models here.


class Department(models.Model):


  depts = (
    ('CS', 'Computer Science'),
    ('CIS', 'Computer Information Systems'),
    ('BIT', 'Business Information Technology'),
    ('DS', 'Data Science'),
    ('AI', 'Artificial Intelligence'),
    ('CyS', 'Cyber Security'),
  )
  
  id                  = models.AutoField(primary_key=True)
  dept_name           = models.CharField(max_length=30, choices=depts)
  no_of_stud_in_dept  = models.PositiveSmallIntegerField(default=0)
  no_of_stu_exceed_90 = models.PositiveSmallIntegerField(default=0)
  start               = models.DateField(editable=True, default='')
  end                 = models.DateField(editable=True, default='')


  def __str__(self):
    return self.dept_name