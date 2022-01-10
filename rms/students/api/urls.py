  
from django.urls import path
from .views import (
   create_student,
   update_student,
   create_student_result,
   update_student_result
 
)

urlpatterns = [
    path('create/student', create_student),
    path('update/student/<int:id>', update_student),
    path('create/student_result', create_student_result),
    path('update/student_result/<int:id>', update_student_result),

]