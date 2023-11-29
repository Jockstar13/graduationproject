from django.shortcuts import render

# Create your views here.

# Login
def index(request):

  context = {
    'title': 'Login',
  }
  return render(request, 'student/pages/index.html', context)


def home(request):
    
  context = {
    'title': 'Home',
    'flag': 'true',
  }
  return render(request, 'student/pages/home.html', context)


def gp(request):
    
  context = {
    'title': 'Graduation Project',
  }
  return render(request, 'student/pages/Graduation-Project/reg-gp.html', context)


def rec_project(request):
    
  context = {
    'title': 'Recommended Project',
  }
  return render(request, 'student/pages/Graduation-Project/rec-project.html', context)


def timeline(request):
    
  context = {
    'title': 'Timeline',
  }
  return render(request, 'student/pages/Graduation-Project/timeline.html', context)


def company(request):
    
  context = {
    'title': 'Internship - Company',
  }
  return render(request, 'student/pages/Internship/company.html', context)


def courses(request):
    
  context = {
    'title': 'Internship - Courses',
  }
  return render(request, 'student/pages/Internship/courses.html', context)


def weekly_form(request):
    
  context = {
    'flag': 'true',
    'title': 'Weekly Following Form',
  }
  return render(request, 'student/pages/Internship/weekly_form.html', context)