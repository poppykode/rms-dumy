from django.urls import path
from .views import  (
    create_course,
    courses,add_course_to_lecturer,
    remove_course_from_lecturer
)

app_name = 'courses'
urlpatterns = [
    path('create',create_course, name='create_course'),
    path('all',courses, name='courses'),
    path('add/course-to-lecturer/<int:l_id>',add_course_to_lecturer, name='add_course_to_lecturer'),
    path('remove/course-from-lecturer/<int:c_id>/<int:l_id>',remove_course_from_lecturer, name='remove_course_from_lecturer'),
]
