from .forms import CompanyForm, CourseForm, LoginForm
from .models import CompanyInternship, CourseInternship, Student
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.







###########################################################
######################### LOGIN ###########################
###########################################################
def index(request):
  if request.user.is_authenticated:
    return redirect('stu-home')

  context = {
    'title': 'Login',
    'flag': True,
    'form': LoginForm(),
  }


  if request.method == 'POST':

    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(request, username=username, password=password)

      if user is not None:
        stu = User.objects.get(username=username)
        stu_data = Student.objects.get(stu=stu)
        if not stu_data.in_internship and not stu_data.in_gp or not stu_data.hours >= 90:
          context.setdefault('allow_error', "You haven't permission to enter website.")
          return render(request, 'student/pages/index.html', context)


        login(request, user)
        return redirect('stu-home')
      else:
        context.setdefault('auth_error', 'Your username or passsword is incorrect.')


    else:
      context.setdefault('valid_error', 'Enter valid Data.')


  return render(request, 'student/pages/index.html', context)




###########################################################
######################### LOGOUT ##########################
###########################################################
def log_out(request):
  logout(request)
  return redirect('login')





###########################################################
########################## HOME ###########################
###########################################################
@login_required(login_url='login')
def home(request):
  try:
    stu = Student.objects.get(stu=request.user)
  except:
    logout(request)
    return redirect('login')

  context = {
    'title': 'Home',
    'flag': True,
    'user': request.user,
  }








  return render(request, 'student/pages/home.html', context)





##############################################################
################### GRADUTATION PROJECT ######################
##############################################################
@login_required(login_url='login')
def gp(request):
  try:
    stu = Student.objects.get(stu=request.user)
  except:
    logout(request)
    return redirect('login')

  context = {
    'title': 'Graduation Project',
  }










  return render(request, 'student/pages/Graduation-Project/reg-gp.html', context)








################################################################
###################### RECOMMENED PROJECT ######################
################################################################
@login_required(login_url='login')
def rec_project(request):
  try:
    stu = Student.objects.get(stu=request.user)
  except:
    logout(request)
    return redirect('login')

  context = {
    'title': 'Recommended Project',
    'user': request.user,
  }








  return render(request, 'student/pages/Graduation-Project/rec-project.html', context)




##############################################################
######################### TIMELINE ###########################
##############################################################
@login_required(login_url='login')
def timeline(request):
  try:
    stu = Student.objects.get(stu=request.user)
  except:
    logout(request)
    return redirect('login')

  context = {
    'title': 'Timeline',
    'user': request.user,
  }









  return render(request, 'student/pages/Graduation-Project/timeline.html', context)





##############################################################
######################### COMPANY FORM #######################
##############################################################
@login_required(login_url='login')
def company(request):
  try:
    stu = Student.objects.get(stu=request.user)
  except:
    logout(request)
    return redirect('login')
    
  context = {
    'title': 'Internship - Company',
    'user': request.user,
  }


  if request.method == 'POST':

    form = CompanyForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      # user = User.objects.get(username=request.user)
      CompanyInternship(student=request.user,
                        company=data['company'], address=data['address'], start=data['start'], end=data['end'],
                        name=data['name'], email=data['email'],
                        description_of_tasks=data['description_of_tasks'], technologies=data['technologies']).save()
      context.setdefault('success', True)
    else:
      context.setdefault('error', True)


  context.setdefault('form', CompanyForm())


  return render(request, 'student/pages/Internship/company.html', context)










#################################################################
######################### COURSE FORM ###########################
#################################################################
@login_required(login_url='login')
def courses(request):
  try:
    stu = Student.objects.get(stu=request.user)
  except:
    logout(request)
    return redirect('login')

  context = {
    'title': 'Internship - Courses',
    'user': request.user,
  }



  if request.method == 'POST':

    form = CourseForm(request.POST, request.FILES)
    if form.is_valid():
      certificate=None
      data = form.cleaned_data
      if 'certificate' in request.FILES.keys():
        certificate=request.FILES['certificate']
      CourseInternship(stu=request.user, course=data['course'], hour=data['hour'],
                        provider=data['provider'], certificate=certificate).save()
      context.setdefault('success', 'The form has been filled out successfully.')
    else:
      context.setdefault('error', 'ERROR: Enter Valid Data.')


  context.setdefault('form', CourseForm())
  return render(request, 'student/pages/Internship/courses.html', context)






##################################################################
######################### REGISTED COURSES #######################
##################################################################
def registered_courses(request):
  context = {
    'title': 'Internship - Courses',
  }

  data = CompanyInternship.objects.filter(user=request.user)



  return render(request, 'student/pages/Internship/courses.html', context)






#################################################################
######################### WEEKLY FORM ###########################
#################################################################
def weekly_form(request):
    
  context = {
    'flag': True,
    'title': 'Weekly Following Form',
  }
  return render(request, 'student/pages/Internship/weekly_form.html', context)


