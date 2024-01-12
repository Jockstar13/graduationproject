from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Student)
admin.site.register(StudentNotification)

# Graduation Project
admin.site.register(GraduationProject)
admin.site.register(StudentRating)
admin.site.register(RecommendedProject)
admin.site.register(GraduationDetails)

admin.site.register(TimlineFiles)
admin.site.register(Timeline)

# Internship
admin.site.register(CompanyInternship)
admin.site.register(CourseInternship)
admin.site.register(WeeklyFollowing)