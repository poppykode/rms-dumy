from django.urls import path

from .views import(
    students,
    student_details,
    archieve,
    achieves

)

app_name = 'students'
urlpatterns = [
    path('all',students, name='students'),
    path('details/<int:pk>/<str:student_id>',student_details, name='student_details'),
    path('achieve/<str:typ>/<str:item_id>/<int:student_id>',archieve, name='archieve'),
    path('all/achieves',achieves, name='achieves'),
]