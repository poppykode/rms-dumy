from django.urls import path

from .views import(
    departments,
    create_department,
    add_department_to_lecturer,
    remove_department_from_lecturer
)

app_name = 'departments'
urlpatterns = [
    path('create',create_department, name='create_department'),
    path('all',departments, name='departments'),
    path('add/department-to-lecturer/<int:l_id>',add_department_to_lecturer, name='add_department_to_lecturer'),
    path('remove/department-from-lecturer/<int:d_id>/<int:l_id>',remove_department_from_lecturer, name='remove_department_from_lecturer'),
]
