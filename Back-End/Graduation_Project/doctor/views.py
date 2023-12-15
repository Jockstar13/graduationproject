from .forms import LoginForm
from .models import Doctor
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.





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
      job_num  = form.cleaned_data.get('job_number')

      user     = authenticate(request, username=username, password=password)
      if user is not None:
        try:
          doc = User.objects.get(username=username)
          doc_data = Doctor.objects.get(doc=doc)
          if str(doc_data.job_number) == job_num:

            login(request, user)
            return redirect('home')
          else:
            context.setdefault('auth_error', 'Your username or passsword or job number is incorrect.')

        except:
          context.setdefault('allow_error', "You haven't permission to enter website.")
      else:
        context.setdefault('auth_error', 'Your username or passsword or job number is incorrect.')
    else:
      context.setdefault('valid_error', 'Enter valid Data.')


  return render(request, 'doctor/pages/index.html', context)







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
  try:
    doc_data = Doctor.objects.get(doc=request.user)
  except:
    logout(request)
    return redirect('signin')


  context = {
    'title': 'Home',
    'flag': 'true',
    'user': request.user,
  }
  return render(request, 'doctor/pages/home.html', context)







############################################################
########################## Teams ###########################
############################################################
@login_required(login_url='signin')
def teams(request):

  try:
    doc_data = Doctor.objects.get(doc=request.user)
  except:
    logout(request)
    return redirect('signin')
  
  
  context = {
    'title': 'Graduation Project Teams',
    'user': request.user,
  }
  return render(request, 'doctor/pages/Graduation-Project/teams.html', context)








###########################################################
###################### Team Details #######################
###########################################################
@login_required(login_url='signin')
def team_details(request):
  try:
    doc_data = Doctor.objects.get(doc=request.user)
  except:
    logout(request)
    return redirect('signin')

  
  context = {
    'title': 'Graduation Project Teams',
    'user': request.user,
  }
  return render(request, 'doctor/pages/Graduation-Project/team-details.html', context)







###########################################################
###################### Student List #######################
###########################################################
@login_required(login_url='signin')
def stu_list(request):
  try:
    doc_data = Doctor.objects.get(doc=request.user)
  except:
    logout(request)
    return redirect('signin')



  context = {
    'title': 'Students List',
    'user': request.user,
  }
  return render(request, 'doctor/pages/Internship/students-list.html', context)






###########################################################
######################### Report ##########################
###########################################################
@login_required(login_url='signin')
def report(request):
  try:
    doc_data = Doctor.objects.get(doc=request.user)
  except:
    logout(request)
    return redirect('signin')



  context = {
    'title': 'Internship Report',
    'user': request.user,
  }
  return render(request, 'doctor/pages/Internship/report.html', context)