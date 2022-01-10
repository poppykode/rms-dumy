from django.contrib import admin
from .models import Department, LecturerDepartment

# Register your models here.
admin.site.register(Department)
admin.site.register(LecturerDepartment)
