from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='stu-home'),
    path('login/', views.index, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('graduation-project/', views.gp, name='gp'),
    path('graduation-project/recommended-project/', views.rec_project, name='rec-project'),
    path('graduation-project/timeline', views.timeline, name='timeline'),
    path('Internship/company-form', views.company, name='company'),
    path('Internship/courses-form', views.courses, name='courses'),
    path('weekly-following-form', views.weekly_form, name='weekly_form'),
]
