from rest_framework import serializers
from students.models import Student,StudentResult

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'student_id',
            'course',
            'student_id_number',
            'national_id_number',
            'first_name',
            'last_name',
            'dob',
            'phone_number',
            'religion',
            'next_of_kin',
            'relationship',
            'next_of_kin_phone_number',
            'address'
            )

class StudentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentResult
        fields = (
            'student_id',
            'student_result_id',
            'student',
            'code',
            'module_name',
            'mark',
            'grade',
            'gpe',
            'credits'
            )