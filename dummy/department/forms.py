from django import forms
from django.contrib.admin import widgets

from .models import Department, LecturerDepartment


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ("name",)

class LecturerDepartmentForm(forms.ModelForm):
    class Meta:
        model = LecturerDepartment
        fields = ("department",)