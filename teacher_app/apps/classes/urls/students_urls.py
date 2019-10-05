from django.urls import path
from teacher_app.apps.classes.views.studentviews import (
    AddStudentView,
    ViewStudentsOfClass,
    EditStudentDetailView
)
urlpatterns = [
    path('add_student/', AddStudentView.as_view(), name="add_new_student"),
    path('class/<str:class_name>/',
         ViewStudentsOfClass.as_view(), name="list_students_of_class"),
    path('<str:reg_num>/edit',
         EditStudentDetailView.as_view(), name="edit_student_details"),
]
