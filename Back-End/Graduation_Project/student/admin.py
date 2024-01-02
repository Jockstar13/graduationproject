from django.contrib import admin
from .models import Student, CompanyInternship, CourseInternship, WeeklyFollowing, GraduationProject, Timeline, StudentNotification

# Register your models here.

admin.site.register(Student)
admin.site.register(StudentNotification)

# Graduation Project
admin.site.register(GraduationProject)
admin.site.register(Timeline)

# Internship
admin.site.register(CompanyInternship)
admin.site.register(CourseInternship)
admin.site.register(WeeklyFollowing)