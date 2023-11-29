from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='signin'),
    path('graduation-project/teams', views.teams, name='teams'),
    path('graduation-project/team-details', views.team_details, name='team-details'),
    path('internship/student-list', views.stu_list, name='stu-list'),
    path('internship/report', views.report, name='report'),
]