from django.contrib import admin
from .models import Student, CompanyInternship, CourseInternship, WeeklyFollowing

# Register your models here.

admin.site.register(Student)
admin.site.register(CompanyInternship)
admin.site.register(CourseInternship)
admin.site.register(WeeklyFollowing)