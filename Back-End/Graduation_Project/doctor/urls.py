from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.index, name='signin'),
    path('logout/', views.log_out, name='log_out'),

    # Graduation Project
    path('graduation-project/teams', views.teams, name='teams'),
    path('graduation-project/team-details/<str:pk>', views.team_details, name='team-details'),

    # Internship
    path('internship/student-list', views.stu_list, name='stu-list'),
    path('internship/report/<str:pk>', views.report, name='report'),

    # Approve and Dissapprove Internship
    path('internship/app_company/<str:pk>', views.app_company, name='app_company'),
    path('internship/dissapp_company/<str:pk>', views.disapp_company, name='disapp_company'),
    path('internship/app_courses/<str:pk>', views.app_courses, name='app_courses'),
    path('internship/dissapp_courses/<str:pk>', views.disapp_courses, name='disapp_courses'),

    # Notification
    path('notification/<str:pk>', views.redirect_notification, name='redirect_notification'),
    path('read_all_notification', views.read_all_notifi, name='read_all'),
]