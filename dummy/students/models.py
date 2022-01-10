from django.db import models
from courses.models import Course
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Student (models.Model):
    course =  models.ForeignKey(Course,on_delete=models.CASCADE,related_name="course_student")
    student_id_number = models.CharField(max_length=255) 
    first_name = models.CharField(max_length=255) 
    last_name = models.CharField(max_length=255) 
    national_id_number = models.CharField(max_length=255) 
    dob = models.DateField()
    phone_number = models.CharField(max_length=255) 
    religion = models.CharField(max_length=255)
    next_of_kin = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    next_of_kin_phone_number = models.CharField(max_length=255)
    address = models.TextField()
    is_deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_id_number

    class Meta:
        ordering = ["-timestamp", ]

class StudentResult(models.Model):
    student =  models.ForeignKey(Student,on_delete=models.CASCADE,related_name="student_result_student")
    code = models.CharField(max_length=255) 
    module_name = models.CharField(max_length=255) 
    mark = models.CharField(max_length=255) 
    grade = models.CharField(max_length=255) 
    gpe = models.CharField(max_length=255) 
    credits = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.student_id_number

    class Meta:
        ordering = ["-timestamp", ]

class StudentCourseWork(models.Model):
    student =  models.ForeignKey(Student,on_delete=models.CASCADE,related_name="student_course_work_student")
    quizz_mark = models.CharField(max_length=255) 
    quizz_total = models.CharField(max_length=255) 
    group_mark = models.CharField(max_length=255) 
    group_total = models.CharField(max_length=255) 
    presentation_mark = models.CharField(max_length=255) 
    presentation_total = models.CharField(max_length=255) 
    test_mark = models.CharField(max_length=255) 
    test_total = models.CharField(max_length=255) 
    final_mark =models.CharField(max_length=255) 
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.student_id_number

    class Meta:
        ordering = ["-timestamp", ]





