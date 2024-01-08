from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='stu-home'),
    path('login/', views.index, name='login'),
    path('logout/', views.log_out, name='logout'),

    # Graduation Project
    path('graduation-project/', views.gp, name='gp'),
    path('graduation-project/recommended-project/', views.rec_project, name='rec-project'),
    path('graduation-project/timeline', views.timeline, name='timeline'),

    # Internship
    path('Internship/company-form', views.company, name='company'),
    path('delete_company', views.delete_company, name='delete_company'),
    
    path('Internship/courses-form', views.courses, name='courses'),
    path('update_course/<str:pk>', views.update_courses, name='update_courses'),
    path('delete_course/<str:pk>', views.delete_courses, name='delete_courses'),

    path('weekly-following-form/<str:student>', views.weekly_form, name='weekly_form'),
    path('close', views.close, name='close'),


    # Notification
    path('notification/<str:pk>', views.redirect_notifi, name='redirect_notifi'),
    path('read_all_notification', views.read_all_notifi, name='read_all_notifi'),
]


handler404 = 'student.views.handling_404'