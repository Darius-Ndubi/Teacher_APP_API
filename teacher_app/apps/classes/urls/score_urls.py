from django.urls import path

from teacher_app.apps.classes.views.scoreviews import (
    TotAveScorePerStudentView,
    TotAveScorePerClassView
)

urlpatterns = [
    path('student/<str:reg_num>/', TotAveScorePerStudentView.as_view(),
         name="student_total_average"),
    path('class/<str:class_name>/', TotAveScorePerClassView.as_view(),
         name="class_total_average"),
]