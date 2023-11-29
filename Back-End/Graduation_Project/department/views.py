from django.shortcuts import render

# Create your views here.



def login(request):
  
  context = {
    'title': 'Login',
    'flag': 'true',
  }
  return render(request, 'department/pages/index.html', context)


def dashboard(request):
  
  context = {
    'title': 'Dashboard',
  }
  return render(request, 'department/pages/dashboard.html', context)


def exceed90(request):
  
  context = {
    'title': 'Students That exceed 90 hours',
  }
  return render(request, 'department/pages/Graduation-Project/exceed-90.html', context)


def team_details(request):
  
  context = {
    'title': 'Team Details',
  }
  return render(request, 'department/pages/Graduation-Project/team-details.html', context)


def teams(request):
  
  context = {
    'title': 'List of Teams',
  }
  return render(request, 'department/pages/Graduation-Project/teams.html', context)


def in_internship(request):
  
  context = {
    'title': 'Students in Internship',
  }
  return render(request, 'department/pages/Internship/in-internship.html', context)


def report(request):
  
  context = {
    'title': 'Report',
  }
  return render(request, 'department/pages/Internship/report.html', context)