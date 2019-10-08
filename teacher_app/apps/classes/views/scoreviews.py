from django.db.models import Sum

from rest_framework import status
from rest_framework.generics import (
    RetrieveAPIView
)
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework.response import Response


from teacher_app.apps.classes.serializers.student_serializers import (
    AddStudentSerializer
)
from teacher_app.apps.classes.serializers.class_serializer import (
    ClassSerializer
)
from teacher_app.apps.classes.models import (
    StudentSubjectMath,
    StudentSubjectEng
)


class TotAveScorePerStudentView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, reg_num):
        AddStudentSerializer.check_if_student_exists(reg_num)

        math_score = StudentSubjectMath.objects.get(student_reg_num=reg_num)
        eng_score = StudentSubjectEng.objects.get(student_reg_num=reg_num)

        total_score = math_score.score + eng_score.score

        average_score = total_score / 2.0

        response_message = {
            "Total score": total_score,
            "Average score": average_score
        }

        return Response(response_message, status=status.HTTP_200_OK)


class TotAveScorePerClassView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, class_name):
        ClassSerializer.check_if_class_exists(class_name)

        math_scores_all_students = StudentSubjectMath.objects.filter(
            className=class_name)
        eng_scores_all_students = StudentSubjectEng.objects.filter(
            className=class_name
        )

        math_score = math_scores_all_students.values(
            'score').aggregate(Sum('score')).get('score__sum')
        
        eng_score = eng_scores_all_students.values(
            'score').aggregate(Sum('score')).get('score__sum')

        avg_score = (math_score + eng_score + 0.0)/(
            math_scores_all_students.count()+eng_scores_all_students.count())

        response_message = {
                "total score": math_score + eng_score,
                "Average score": avg_score
            }

        return Response(response_message, status=status.HTTP_200_OK)
