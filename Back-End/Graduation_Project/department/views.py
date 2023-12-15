from .forms import LoginForm
from doctor.models import Doctor
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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
  try:
    doc = Doctor.objects.get(doc=request.user)
    if doc.permission != 'doc&head':
      logout(request)
      return redirect('login-form')
  except:
    logout(request)
    return redirect('login-form')




  context = {
    'title': 'Dashboard',
  }
  return render(request, 'department/pages/dashboard.html', context)







##########################################################
####################### Exceed 90 ########################
##########################################################
@login_required(login_url='login-form')
def exceed90(request):
  try:
    doc = Doctor.objects.get(doc=request.user)
    if doc.permission is not 'doc&head' or 'sec':
      logout(request)
      return redirect('login-form')
  except:
    logout(request)
    return redirect('login-form')


  context = {
    'title': 'Students That exceed 90 hours',
  }
  return render(request, 'department/pages/Graduation-Project/exceed-90.html', context)








###########################################################
###################### Team Details #######################
###########################################################
@login_required(login_url='login-form')
def team_details(request):
  try:
    doc = Doctor.objects.get(doc=request.user)
    if doc.permission is not 'doc&head' or 'sec':
      logout(request)
      return redirect('login-form')
  except:
    logout(request)
    return redirect('login-form')
  


  context = {
    'title': 'Team Details',
  }
  return render(request, 'department/pages/Graduation-Project/team-details.html', context)







##########################################################
######################### Teams ##########################
##########################################################
@login_required(login_url='login-form')
def teams(request):
  try:
    doc = Doctor.objects.get(doc=request.user)
    if doc.permission is not 'doc&head' or 'sec':
      logout(request)
      return redirect('login-form')
  except:
    logout(request)
    return redirect('login-form')
  


  context = {
    'title': 'List of Teams',
  }
  return render(request, 'department/pages/Graduation-Project/teams.html', context)








############################################################
###################### In Internship #######################
############################################################
@login_required(login_url='login-form')
def in_internship(request):
  try:
    doc = Doctor.objects.get(doc=request.user)
    if doc.permission is not 'doc&head' or 'sec':
      logout(request)
      return redirect('login-form')
  except:
    logout(request)
    return redirect('login-form')


  context = {
    'title': 'Students in Internship',
  }
  return render(request, 'department/pages/Internship/in-internship.html', context)







###########################################################
######################### Report ##########################
###########################################################
@login_required(login_url='login-form')
def report(request):
  try:
    doc = Doctor.objects.get(doc=request.user)
    if doc.permission is not 'doc&head' or 'sec':
      logout(request)
      return redirect('login-form')
  except:
    logout(request)
    return redirect('login-form')


  context = {
    'title': 'Report',
  }
  return render(request, 'department/pages/Internship/report.html', context)