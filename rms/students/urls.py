from django.urls import path

from .views import(
    students,
    student_details,
    archieve,
    achieves,
    pdf_report_create,
    update_achieve

)

app_name = 'students'
urlpatterns = [
    path('all',students, name='students'),
    path('details/<int:pk>/<str:student_id>',student_details, name='student_details'),
    path('achieve/<str:typ>/<str:item_id>/<int:student_id>',archieve, name='archieve'),
    path('update-achieve/<str:typ>/<str:item_id>/<int:student_id>/<int:student_pk>',update_achieve, name='update_achieve'),
    path('all/achieves',achieves, name='achieves'),
    path('create-pdf/<int:id>',pdf_report_create, name='pdf_report_create'),
]
