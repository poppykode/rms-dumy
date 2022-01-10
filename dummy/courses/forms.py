from django import forms
from django.contrib.admin import widgets
from .models import Course, LecturerCourse


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("name",)

class LecturerCourseForm(forms.ModelForm):
    class Meta:
        model = LecturerCourse
        fields = ("course",)