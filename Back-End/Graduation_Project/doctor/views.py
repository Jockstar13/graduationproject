from .forms import LoginForm, AppCompForm, DisappCompForm, AppCorForm, DisappCorForm
from .models import Doctor, DoctorNotification
from student.models import Student, CompanyInternship, CourseInternship, GraduationProject, Timeline, StudentNotification, WeeklyFollowing
from django.shortcuts import render, redirect
from department.models import Department, DepartmentNotification
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.



################# Check If Doctor #################
def is_doctor(request):
  try:
    doc_data = Doctor.objects.get(doc=request.user)
    return doc_data
  except:
    logout(request)
    return redirect('signin')






# ############# Send Notification to Department ###############
def notify_department(department, subject, message, url_name, query_pk=''):
  try:
    DepartmentNotification(department=department, subject=subject, message=message, url_name=url_name, query_pk=query_pk).save()
  except:
    DepartmentNotification(department=department, subject=subject, message=message, url_name=url_name).save()




############### Send Notification to Doctor #################
def notify_student(student, subject, message, url_name, query_pk=''):
  try:
    StudentNotification(student=student, subject=subject, message=message, url_name=url_name, query_pk=query_pk).save()
  except:
    StudentNotification(student=student, subject=subject, message=message, url_name=url_name).save()






##################### Get Notification ####################
def get_notification(request):
  doctor_rec = is_doctor(request)
  all_notifications = DoctorNotification.objects.filter(doctor=doctor_rec.doc).order_by('-id')

  there_is = False
  for n in all_notifications:
    if not n.is_read:
      there_is = True
      break

  return {'all_notifications': all_notifications, 'there_is': there_is}




################### Redirect Notification ##################
def redirect_notification(request, pk):
  try:
    n = DoctorNotification.objects.get(id=pk)
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
def read_all_notifi(request):
  all_n = DoctorNotification.objects.all()
  
  for n in all_n:
    n.is_read = True
    n.save()
  else:
    return redirect(request.META.get('HTTP_REFERER'))








############################################################
########################## Login ###########################
############################################################
def index(request):
  if request.user.is_authenticated:
    redirect('home')

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
      # job_num  = form.cleaned_data.get('job_number')

      user     = authenticate(request, username=username, password=password)
      if user is not None:
        try:
          doc = User.objects.get(username=username)
          doc_data = Doctor.objects.get(doc=doc)
          # if str(doc_data.job_number) == job_num:

          # else:
          #   context.setdefault('auth_error', 'Your username or passsword or job number is incorrect.')

          login(request, user)
          return redirect('home')
        except:
          context.setdefault('allow_error', "You haven't permission to enter website.")
      else:
        context.setdefault('auth_error', 'Your username or passsword is incorrect.')
    else:
      context.setdefault('valid_error', 'Enter valid Data.')


  return render(request, 'doctor/pages/index.html', context)
####################################################################################################
####################################################################################################






###########################################################
######################### LOGOUT ##########################
###########################################################
def log_out(request):
  logout(request)
  return redirect('signin')







###########################################################
########################## HOME ###########################
###########################################################
@login_required(login_url='signin')
def home(request):
  doctor_rec = is_doctor(request)


  context = {
    'title': 'Home',
    'flag': 'true',
    'user': request.user,
    'notifications': get_notification(request),
  }
  return render(request, 'doctor/pages/home.html', context)







############################################################
########################## Teams ###########################
############################################################
@login_required(login_url='signin')
def teams(request):
  doctor_rec = is_doctor(request)

  context = {
    'title'        : 'Graduation Project Teams',
    'user'         : request.user,
    'notifications': get_notification(request),
  }



  all_teams = GraduationProject.objects.filter(email_1=doctor_rec.doc.email) | GraduationProject.objects.filter(email_2=doctor_rec.doc.email) 


  teams = {}
  for i in all_teams:
    teams.setdefault(i, i.members.all())
  else:
    context.setdefault('teams', teams)

  return render(request, 'doctor/pages/Graduation-Project/teams.html', context)








###########################################################
###################### Team Details #######################
###########################################################
@login_required(login_url='signin')
def team_details(request, pk):
  doctor_rec = is_doctor(request) 

  context = {
    'title': 'Graduation Project Teams',
    'user': request.user,
    'notifications': get_notification(request),
  }

  # Check if the team is exist
  try:
    team = GraduationProject.objects.get(id=pk)

    if team.email_1 != doctor_rec.doc.email and team.email_1 != doctor_rec.doc.email:
      return redirect('teams')
    else:
      context.setdefault('team', team)


    members = {}
    for member in team.members.all():
      try:
        student = Student.objects.get(stu=member)
        members.setdefault(member, student)
      except ObjectDoesNotExist:
        pass

    context.setdefault('members', members)
  except ObjectDoesNotExist:
    return redirect('teams')
  except ValueError:
    return redirect('teams')




  # Get all posts of the team from timeline.
  try:
    posts = Timeline.objects.filter(team=team).order_by('-id')
    context.setdefault('posts', posts)
  except:
    pass


  return render(request, 'doctor/pages/Graduation-Project/team-details.html', context)







###########################################################
###################### Student List #######################
###########################################################
@login_required(login_url='signin')
def stu_list(request):
  doctor_rec = is_doctor(request) 


  # Get Students that belogns to authenticated Doctor.
  try:
    students = Student.objects.filter(doc_superviser=doctor_rec)
  except ObjectDoesNotExist:
    pass


  context = {
    'title': 'Students List',
    'user': request.user,
    'students': students,
    'notifications': get_notification(request),
  }
  return render(request, 'doctor/pages/Internship/students-list.html', context)






###########################################################
######################### Report ##########################
###########################################################
@login_required(login_url='signin')
def report(request, pk):
  doctor_rec = is_doctor(request) 




  # Get Student Info
  try:
    student = Student.objects.get(id=pk, doc_superviser=doctor_rec)
    user    = User.objects.get(username=student.stu)
  except:
    return redirect('stu-list')

  # Get Student Company Internship Info
  try:
    stu_company = CompanyInternship.objects.get(student=user)
  except ObjectDoesNotExist:
    stu_company = None


  # Get Student Courses Internship Info
  stu_courses = CourseInternship.objects.filter(stu=user)



  # Get weekly reports
  report = WeeklyFollowing.objects.filter(stu_user=user)
  weeks_name = report.all().values_list('week', flat=True).distinct()



  context = {
    'title'        : 'Internship Report',
    'user'         : request.user,
    'student'      : student,
    'stu_company'  : stu_company,
    'stu_courses'  : stu_courses,
    'appcomform'   : AppCompForm(),
    'disappcomform': DisappCompForm(),
    'appcorform'   : AppCorForm(),
    'disappcorform': DisappCorForm(),
    'notifications': get_notification(request),
    'weeks'        : report,
    'weeks_name'   : weeks_name,
  }
  return render(request, 'doctor/pages/Internship/report.html', context)




def app_company(request, pk):
  doctor_rec = is_doctor(request) 

  if request.method == 'POST':

    form = AppCompForm(request.POST)
    if form.is_valid():
      s = Student.objects.get(id=pk)
      s_company = CompanyInternship.objects.get(student=s.stu)
      s_company.int_com_acc = True
      s_company.doc_note = form.cleaned_data['app_company']
      s_company.save()


      # Send Notification to the Student
      message = f'{doctor_rec.doc.first_name} {doctor_rec.doc.first_name} approve your company internship.'
      notify_student(s.stu, subject='Company - Internship Approval', message=message, url_name='company')


      dept_name = Department.objects.get(dept_name=doctor_rec.department)
      message_dept = f'{doctor_rec.doc.first_name} {doctor_rec.doc.first_name} approve {s.stu.first_name} {s.stu.last_name} internship.'
      notify_department(dept_name, subject='Company - Internship Approval', message=message_dept, url_name='student-report', query_pk=pk)


      return redirect('report', pk)







def disapp_company(request, pk):
  doctor_rec = is_doctor(request)


  if request.method == 'POST':

    form = DisappCompForm(request.POST)
    if form.is_valid():
      s = Student.objects.get(id=pk)
      s_company = CompanyInternship.objects.get(student=s.stu)
      s_company.int_com_acc = False
      s_company.doc_note = form.cleaned_data['dis_company']
      s_company.save()



      # Send Notification to the Student
      message = f'{doctor_rec.doc.first_name} {doctor_rec.doc.first_name} disapprove your company internship.'
      notify_student(s.stu, subject='Company - Internship Disapproval', message=message, url_name='company')
      
      return redirect('report', pk)









def app_courses(request, pk):
  doctor_rec = is_doctor(request)


  if request.method == 'POST':

    form = request.POST

    for value in form.values():
      if not value.isspace():
        s_course = CourseInternship.objects.get(id=pk)
        s_course.int_cor_acc = True
        s_course.doc_note = value
        s_course.save()




    else:
      student = Student.objects.get(stu=s_course.stu)

      # Send Notification to the Student
      message = f'{doctor_rec.doc.first_name} {doctor_rec.doc.first_name} approve your course internship.'
      notify_student(s_course.stu, subject='Courses - Internship Approval', message=message, url_name='courses')

      dept_name = Department.objects.get(dept_name=doctor_rec.department)
      message_dept = f'{doctor_rec.doc.first_name} {doctor_rec.doc.first_name} approve {student.stu.first_name} {student.stu.last_name} course.'
      notify_department(dept_name, subject='Courses - Internship Approval', message=message_dept, url_name='student-report', query_pk=student.pk)
      return redirect('report', student.pk)








def disapp_courses(request, pk):
  doctor_rec = is_doctor(request)

  if request.method == 'POST':

    form = request.POST

    for value in form.values():
      if not value.isspace():
        s_course = CourseInternship.objects.get(id=pk)
        s_course.int_cor_acc = False
        s_course.doc_note = value
        s_course.save()



      # Send Notification to the Student
      message = f'{doctor_rec.doc.first_name} {doctor_rec.doc.first_name} disapprove your course internship.'
      notify_student(s_course.stu, subject='Courses - Internship Disapproval', message=message, url_name='courses')

      student = Student.objects.get(stu=s_course.stu).pk
    else:
      return redirect('report', student)




################################################################
##################### NOT FOUND PAGE 404 #######################
################################################################
def handling_404(request, exception):
  return render(request, '404.html', {'flag', True},status=404)
####################################################################################################
####################################################################################################