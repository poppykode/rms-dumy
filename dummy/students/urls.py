from django.urls import path

from .views import(
    students,
    create_student,
    add_results_to_student,
    student_details,
    add_course_work_marks_to_student
)

app_name = 'students'
urlpatterns = [
    path('all',students, name='students'),
    path('create',create_student, name='create_student'),
    path('details/<int:pk>',student_details, name='student_details'),
    path('add/results-to-student/<int:s_id>',add_results_to_student, name='add_results_to_student'),
    path('add/course-work-marks-to-student/<int:s_id>',add_course_work_marks_to_student, name='add_course_work_marks_to_student'),
]
