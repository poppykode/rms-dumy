from django import forms
from .models import Student, StudentResult, StudentCourseWork


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4, },),
            'dob': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date', 'data-date-format': 'YYYY-MM-DD'}),
            # 'phone_number': forms.TextInput(attrs={'type': 'date', 'data-date-format': 'YYYY-MM-DD'}),
        }
        fields = (
            "first_name",
            "last_name",
            "national_id_number",
            "dob",
            "phone_number",
            "religion",
            "next_of_kin",
            "relationship",
            "next_of_kin_phone_number",
            "address",
            "course",
            )

class StudentResultForm(forms.ModelForm):
    class Meta:
        model = StudentResult
        fields =(
            "code",
            "module_name" ,
            "mark" ,
            "grade",
            "gpe",
            "credits",
        )

class StudentCourseWorkForm(forms.ModelForm):
    class Meta:
        model = StudentCourseWork
        fields =(
            "quizz_mark",
            "quizz_total" ,
            "group_mark" ,
            "group_total",
            "presentation_mark",
            "presentation_total",
            "test_mark",
            "test_total",
        )

