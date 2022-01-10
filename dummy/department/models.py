from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Department (models.Model):
    name = models.CharField(max_length=255) 
    is_deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class LecturerDepartment (models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE,related_name="lecturer_department_lecturer")
    department =  models.ForeignKey(Department,on_delete=models.CASCADE,related_name="department_lecturer")
    is_deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.department.name
