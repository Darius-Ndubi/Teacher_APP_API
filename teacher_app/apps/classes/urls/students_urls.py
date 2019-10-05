from django.urls import path
from ..views.studentviews import (
    AddStudentView,
    ViewStudentsOfClass
)

urlpatterns = [
    path('add_student/', AddStudentView.as_view(), name="add_new_student"),
    path('class/<str:class_name>/',
         ViewStudentsOfClass.as_view(), name="list_students_of_class")
]
