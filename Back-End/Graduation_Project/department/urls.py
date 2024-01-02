from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login', views.signin, name='login-form'),
    path('logout', views.signout, name='signout'),

    # graduation Project
    path('exceed-90-hours', views.exceed90, name='exceed90'),
    path('list-of-teams', views.teams, name='gp-teams'),
    path('team-details/<str:pk>', views.team_details, name='team_details'),

    # Internship
    path('students-in-internship', views.in_internship, name='in-internship'),
    path('report/<str:pk>', views.report, name='student-report'),

    # Notification
    path('notification/<str:pk>', views.redirect_notification, name='redirect-notification'),
    path('read_all_notification', views.read_all_notification, name='read_all_notification'),
]