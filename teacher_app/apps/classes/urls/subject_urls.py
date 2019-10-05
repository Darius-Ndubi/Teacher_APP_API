from django.urls import path
from teacher_app.apps.classes.views.subjectviews import (
    AssignStudentSubjectView,
    ViewStudentSubjects
)
urlpatterns = [
    path('assign/', AssignStudentSubjectView.as_view(),
         name="give_student_subject"),  
    path('<str:reg_num>/', ViewStudentSubjects.as_view(),
         name="subjects_taken_by_student"),
]
