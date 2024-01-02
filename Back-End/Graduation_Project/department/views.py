from .forms import LoginForm, DashboardForm
from .models import Department, DepartmentNotification
from doctor.models import Doctor, DoctorNotification
from student.models import Student, CompanyInternship, CourseInternship, GraduationProject, StudentNotification
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

################# Check If Head #################
def is_head(request):
  try:
    doc = Doctor.objects.get(doc=request.user)
    if doc.permission != 'doc&head':
      logout(request)
      return redirect('login-form')
    else:
      return doc
  except:
    logout(request)
    return redirect('login-form')






# ############# Send Notification to Department ###############
def notify_doctor(doctor, subject, message, url_name):
  DoctorNotification(doctor=doctor, subject=subject, message=message, url_name=url_name).save()




############### Send Notification to Doctor #################
def notify_student(student, subject, message, url_name):
  StudentNotification(student=student, subject=subject, message=message, url_name=url_name).save()









##################### Get Notification ####################
def get_notification(request):
  try:
    head_rec = is_head(request)
  except AttributeError:
    return redirect('login-form')


  dept_name = Department.objects.get(dept_name=head_rec.department)
  all_notifications = DepartmentNotification.objects.filter(department=dept_name).order_by('-id')

  there_is = False
  for n in all_notifications:
    if not n.is_read:
      there_is = True
      break

  return {'all_notifications': all_notifications, 'there_is': there_is}




################### Redirect Notification ##################
def redirect_notification(request, pk):
  try:
    n = DepartmentNotification.objects.get(id=pk)
    n.is_read = True
    n.save()

    if n.query_pk:
      query = n.query_pk
      return redirect(n.url_name, query)
    else:
      return redirect(n.url_name)
  except ObjectDoesNotExist:
    pass


################### Read All Notification ##################
def read_all_notification(request):
  all_n = DepartmentNotification.objects.all()
  
  for n in all_n:
    n.is_read = True
    n.save()
  else:
    return redirect(request.META.get('HTTP_REFERER'))






# Create your views here.

###########################################################
######################### Signin ##########################
###########################################################
def signin(request):
  if request.user.is_authenticated:
    return redirect('dashboard')

  context = {
    'title': 'Login',
    'flag': 'true',
    'form': LoginForm(),
  }

  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      job_num  = form.cleaned_data.get('job_number')

      user = authenticate(request, username=username, password=password)
      if user is not None:
        try:
          doc = User.objects.get(username=username)
          doc_data = Doctor.objects.get(doc=doc)
          if (str(doc_data.job_number) == job_num):
            if  doc_data.permission == 'doc&head':
              login(request, user)
              return redirect('dashboard')
            else:
              context.setdefault('allow_error', "You haven't permission to enter website.")
          else:
            context.setdefault('auth_error', 'Your username or passsword or job number is incorrect.')

        except:
          context.setdefault('allow_error', "You haven't permission to enter website.")
      else:
        context.setdefault('auth_error', 'Your username or passsword or job number is incorrect.')
    else:
      context.setdefault('valid_error', 'Enter valid Data.')

  return render(request, 'department/pages/index.html', context)






##########################################################
######################## Signout #########################
##########################################################
def signout(request):
  logout(request)
  return redirect('login-form')







##########################################################
####################### Dashboard ########################
##########################################################
@login_required(login_url='login-form')
def dashboard(request):
  head_rec = is_head(request)

  # Get Department Record
  try:
    department = Department.objects.get(dept_name=head_rec.department)
  except:
    return redirect('login-form')
  returned_data = {
    'start'       : department.start,
    'end'         : department.end,
    'team_mem_num': department.num_team_member,
  }



  # Get Number of School's Student
  all = Student.objects.all().count()

  # Get Number of Department's Student
  dep_stu_num = Student.objects.filter(major=department.dept_name).count()

  # Get Number of Students that Exceed 90 Hours
  exceed90 = Student.objects.filter(hours__gte=90, major=department.dept_name).count()

  # Get Number of Students that Enroll in Internship
  int_stu = Student.objects.filter(in_internship=True, major=department.dept_name).count()

  # Get Number of Students that Enroll in Graduation Project
  gp_stu = Student.objects.filter(in_gp=True, major=department.dept_name).count()

  # Get Number of Students that Expected to Graduate
  major_hour = 132
  last_semester = 16
  complete = major_hour - last_semester
  graduate = Student.objects.filter(hours__gte=complete, major=department.dept_name).count()



  # Starting, ending date and number of team's member
  vaildation_error = ''
  if request.method == 'POST':
    form = DashboardForm(request.POST)
    if form.is_valid():

      data              = form.cleaned_data
      d                 = Department.objects.get(dept_name=department.dept_name)
      d.dept_name       = department.dept_name
      d.start           = data['start']
      d.end             = data['end']
      d.num_team_member = data['team_mem_num']
      d.save()
    else:
      vaildation_error  = 'Enter Vaild Data'

  else:
    form = DashboardForm(returned_data)










  context = {
    'title'           : 'Dashboard',
    'dept'            : department,
    'dep_stu_num'     : dep_stu_num,
    'all'             : all,
    'exceed90'        : exceed90,
    'int_stu'         : int_stu,
    'gp_stu'          : gp_stu,
    'graduate'        : graduate,
    'form'            : form,
    'vaildation_error': vaildation_error,
    'notifications'   : get_notification(request),
  }



  return render(request, 'department/pages/dashboard.html', context)







##########################################################
####################### Exceed 90 ########################
##########################################################
@login_required(login_url='login-form')
def exceed90(request):
  head_rec = is_head(request)

  # Get Department Record
  try:
    department = Department.objects.get(dept_name=head_rec.department)
  except:
    return redirect('login-form')





  # Get Students that exceed 90 Hours
  exceed90   = Student.objects.all().values().filter(hours__gte=90, major=department.dept_name)

  stu=[]

  for item in exceed90:
    stu_dict = {}
    stu_dict.setdefault('in_internship', item['in_internship'])
    stu_dict.setdefault('in_gp', item['in_gp'])
    
    u = User.objects.get(id=item['stu_id'])
    stu_dict.setdefault('username', u.username)
    stu_dict.setdefault('email', u.email)
    stu_dict.setdefault('first_name', u.first_name)
    stu_dict.setdefault('last_name', u.last_name)
    stu.append(stu_dict)





  context = {
    'title'        : 'Students That exceed 90 hours',
    'dept'         : department,
    'stu'          : stu,
    'notifications': get_notification(request),
  }
  return render(request, 'department/pages/Graduation-Project/exceed-90.html', context)








##########################################################
######################### Teams ##########################
##########################################################
@login_required(login_url='login-form')
def teams(request):
  head_rec = is_head(request)

  # Get Department Record
  try:
    department = Department.objects.get(dept_name=head_rec.department)
  except:
    return redirect('login-form')




  # Get all teams that belongs to department
  department_teams = []
  teams = GraduationProject.objects.all()
  for team in teams:
    for member in team.members.all():
      try:
        s = Student.objects.get(stu=member, major=department.dept_name)
        department_teams.append(team)
        break
      except ObjectDoesNotExist:
        pass







  context = {
    'title'           : 'List of Teams',
    'dept'            : department,
    'department_teams': department_teams,
    'notifications'   : get_notification(request),
  }
  return render(request, 'department/pages/Graduation-Project/teams.html', context)








###########################################################
###################### Team Details #######################
###########################################################
@login_required(login_url='login-form')
def team_details(request, pk):
  head_rec = is_head(request)

  # Get Department Record
  try:
    department = Department.objects.get(dept_name=head_rec.department)
  except:
    return redirect('login-form')



  try:
    # Check if the is exists
    team = GraduationProject.objects.get(id=pk)
    members = []
    try:
      for member in team.members.all():
        try:
          student = Student.objects.get(stu=member)
          members.append(student)
        except:
          pass
      else:
        for value in members:
          if value.major == department.dept_name:
            break
        else:
          return redirect('gp-teams')


    except:
      pass
  except ObjectDoesNotExist:
      return redirect('gp-teams')












  context = {
    'title'        : 'Team Details',
    'dept'         : department,
    'team'         : team,
    'members'      : members,
    'notifications': get_notification(request),
  }
  return render(request, 'department/pages/Graduation-Project/team-details.html', context)








############################################################
###################### In Internship #######################
############################################################
@login_required(login_url='login-form')
def in_internship(request):
  head_rec = is_head(request)






  # Get Department Record
  try:
    department = Department.objects.get(dept_name=head_rec.department)
  except:
    return redirect('login-form')


  # Get Doctor Info
  doc_rec = Doctor.objects.all().filter(department=department.dept_name)




  # Set Doctors to Students for Internship
  if request.method == 'POST':
    # Get Student That Register In Internship Course.
    stu_rec = Student.objects.all().filter(major=department.dept_name ,in_internship=True)

    for i in stu_rec:
      if request.POST.get(i.stu.username) != 'None':
        s = Student.objects.get(stu=i.stu)
        u = User.objects.get(username=request.POST.get(i.stu.username, False))
        d = Doctor.objects.get(doc=u)
        s.doc_superviser = d
        s.save()

        # Send Notification to docotor and student
        message = f'Now you are supervisor of {s.stu.first_name} {s.stu.last_name} for internship.'
        notify_doctor(d.doc, 'Internship Supervision', message=message, url_name='stu-list')
        
        message_stu = f'{d.doc.first_name} {d.doc.last_name} is your supervisor in internship this semester.'
        notify_student(s.stu, 'Internship', message_stu, url_name='company')




  # Get Student That Register In Internship Course.
  stu_rec = Student.objects.all().filter(major=department.dept_name ,in_internship=True)





  context = {
    'title'        : 'Students in Internship',
    'dept'         : department,
    'docs'         : doc_rec,
    'stus'         : stu_rec,
    'notifications': get_notification(request),
  }
  return render(request, 'department/pages/Internship/in-internship.html', context)







###########################################################
######################### Report ##########################
###########################################################
@login_required(login_url='login-form')
def report(request, pk):
  head_rec = is_head(request)

  # Get Department Record
  try:
    department = Department.objects.get(dept_name=head_rec.department)
  except:
    return redirect('login-form')


  # Check if Student Record Id Belongs to Department
  try:
    stu      = Student.objects.get(id=pk, major=department.dept_name)
    stu_user = User.objects.get(username=stu.stu.username)
  except ObjectDoesNotExist:
    return redirect('in-internship')


  # Get Student Compnay Internship Info
  try:
    stu_company = CompanyInternship.objects.get(student=stu.stu)
  except:
    stu_company = None


  # Get Student Courses Internship Info
  try:
    stu_course  = CourseInternship.objects.filter(stu=stu.stu)
  except:
    stu_course  = None









  context = {
    'title'        : 'Report',
    'student_user' : stu_user,
    'student_rec'  : stu,
    'stu_company'  : stu_company,
    'stu_course'   : stu_course,
    'dept'         : department,
    'notifications': get_notification(request),
  }
  return render(request, 'department/pages/Internship/report.html', context)