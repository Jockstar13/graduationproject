from django.shortcuts import render

# Create your views here.


# Login
def login(request):
  
  context = {
    'title': 'Login',
    'flag': 'true',
  }
  return render(request, 'doctor/pages/index.html', context)


# Home
def home(request):
  
  context = {
    'title': 'Home',
    'flag': 'true',
  }
  return render(request, 'doctor/pages/home.html', context)


# Graduation Project/ Teams
def teams(request):
  
  context = {
    'title': 'Graduation Project Teams',
  }
  return render(request, 'doctor/pages/Graduation-Project/teams.html', context)


# Graduation Project/ Team Details
def team_details(request):
  
  context = {
    'title': 'Graduation Project Teams',
  }
  return render(request, 'doctor/pages/Graduation-Project/team-details.html', context)


# Internship/ Students List
def stu_list(request):
  
  context = {
    'title': 'Students List',
  }
  return render(request, 'doctor/pages/Internship/students-list.html', context)


# Internship/ Report
def report(request):
  
  context = {
    'title': 'Internship Report',
  }
  return render(request, 'doctor/pages/Internship/report.html', context)