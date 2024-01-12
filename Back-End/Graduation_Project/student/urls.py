from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='stu-home'),
    path('login/', views.index, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),

    # Graduation Project
    path('graduation-project/', views.gp, name='gp'),
    path('graduation-project/recommended-project/', views.rec_project, name='rec-project'),
    path('graduation-project/recommended-project/<str:project_id>', views.project_details, name='project-details'),
    path('graduation-project/timeline', views.timeline, name='timeline'),
    path('delete_timeline/<str:post_id>', views.delete_timeline, name='delete_timeline'),

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
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'student.views.handling_404'