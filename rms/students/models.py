from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Student (models.Model):
    student_id = models.CharField(max_length=255) 
    course =   models.CharField(max_length=255) 
    student_id_number = models.CharField(max_length=255) 
    first_name = models.CharField(max_length=255) 
    last_name = models.CharField(max_length=255) 
    national_id_number = models.CharField(max_length=255) 
    dob = models.CharField(max_length=255) 
    phone_number = models.CharField(max_length=255) 
    religion = models.CharField(max_length=255)
    next_of_kin = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    next_of_kin_phone_number = models.CharField(max_length=255)
    archieved = models.BooleanField(default=False)
    address = models.TextField()
    archieve_id =   models.CharField(max_length=255,blank=True,null=True)
    is_deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_id_number

    class Meta:
        ordering = ["-timestamp", ]

class StudentResult(models.Model):
    student_id = models.CharField(max_length=255) 
    student_result_id = models.CharField(max_length=255) 
    student =  models.CharField(max_length=255) 
    code = models.CharField(max_length=255) 
    module_name = models.CharField(max_length=255) 
    mark = models.CharField(max_length=255) 
    grade = models.CharField(max_length=255) 
    gpe = models.CharField(max_length=255) 
    credits = models.CharField(max_length=255)
    archieved = models.BooleanField(default=False)
    archieve_id =   models.CharField(max_length=255,blank=True,null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.student_id_number

    class Meta:
        ordering = ["-timestamp", ]

class Archieve(models.Model):
    archieve_id = models.CharField(max_length=255)
    typ =  models.CharField(max_length=255) 
    item_id = models.CharField(max_length=255)
    row = models.PositiveIntegerField() 
    bay = models.PositiveIntegerField() 
    shelf =  models.PositiveIntegerField() 
    position = models.CharField(max_length=255) 
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.archieve_id

    class Meta:
        ordering = ["-timestamp", ]