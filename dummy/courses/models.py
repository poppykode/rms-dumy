from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class Course (models.Model):
    name = models.CharField(max_length=255) 
    is_deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class LecturerCourse (models.Model):
    lecturer =  models.ForeignKey(User,on_delete=models.CASCADE,related_name="lecturer_course_lecturer")
    course =  models.ForeignKey(Course,on_delete=models.CASCADE,related_name="course_lecturer")
    is_deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course.name
        