from django.urls import path
from teacher_app.apps.classes.views.subjectviews import (
    AssignStudentSubjectView,
    ViewStudentSubjects,
    FilterStudentSubjectView,
    AssignStudentSubjectScoreView,
)

urlpatterns = [
    path('assign/', AssignStudentSubjectView.as_view(),
         name="give_student_subject"),  
    path('<str:reg_num>/', ViewStudentSubjects.as_view(),
         name="subjects_taken_by_student"),
    path('<str:subject_name>/filter/', FilterStudentSubjectView.as_view(),
        name="Filter_students_by_subject"),
    path('<str:reg_num>/score/', AssignStudentSubjectScoreView.as_view(),
        name="assing_student_subject_score")
]
