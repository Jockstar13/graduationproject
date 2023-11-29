from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login-form'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('exceed-90-hours', views.exceed90, name='exceed90'),
    path('team-details', views.team_details, name='team_details'),
    path('list-of-teams', views.teams, name='gp-teams'),
    path('students-in-internship', views.in_internship, name='in-internship'),
    path('report', views.report, name='student-report'),
]