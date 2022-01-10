from django.contrib import admin
from .models import Student, StudentCourseWork,StudentResult

# Register your models here.
admin.site.register(Student)
admin.site.register(StudentCourseWork)
admin.site.register(StudentResult)

