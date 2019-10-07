from rest_framework import status
from rest_framework import exceptions 

from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView
)
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework.response import Response

from teacher_app.apps.classes.serializers.subject_serializer import (
    SubjectMathSerializer,
    SubjectEngSerializer
)
from teacher_app.apps.classes.serializers.student_serializers import AddStudentSerializer
from teacher_app.apps.classes.models import (
    StudentSubjectMath,
    StudentSubjectEng
)


class AssignStudentSubjectView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        student = AddStudentSerializer.check_if_student_exists(
            request.data['regNumber'])

        student_data = {}
        student_data['student'] = student.id

        SubjectMathSerializer().validate_math_field(subject_math=request.data['maths'])
        SubjectEngSerializer().validate_eng_field(subject_eng=request.data['english'])

        for (key, value) in request.data.items():
            if key.lower() == 'maths' and request.data[key] == 'True':
                student_data['score'] = 0
                student_data['assign'] = True
                student_data['student_reg_num'] = request.data['regNumber']

                math_serialize = SubjectMathSerializer(data=student_data)

                if not math_serialize.is_valid():
                    return Response(
                        math_serialize.errors,
                        status=status.HTTP_400_BAD_REQUEST)
                math_serialize.save()

            elif key.lower() == 'english' and request.data[key] == 'True':
                student_data['score'] = 0
                student_data['assign'] = True
                student_data['student_reg_num'] = request.data['regNumber']
                eng_serialize = SubjectEngSerializer(data=student_data)

                if not eng_serialize.is_valid():
                    return Response(
                        eng_serialize.errors,
                        status=status.HTTP_400_BAD_REQUEST)
                eng_serialize.save()

        response_message = {
            "message": "You have successfully assigned " +
            "{student} to {num_subjects} subjects".format(
                student=request.data['regNumber'],
                num_subjects=len(request.data.items())-1
            )
        }

        return Response(response_message, status=status.HTTP_200_OK)


class ViewStudentSubjects(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, reg_num):
        AddStudentSerializer.check_if_student_exists(reg_num)

        math = StudentSubjectMath.objects.filter(
            student_reg_num=reg_num).exists()

        english = StudentSubjectEng.objects.filter(
            student_reg_num=reg_num).exists()

        data = {}
        if math:
            data['Maths'] = True
        elif english:
            data['English'] = True

        response_message = {
            "subjects": data,
            "message": "Student RegNo:{regNumber} is taking the above subject(s)".format(regNumber=reg_num)
        }

        return Response(response_message, status=status.HTTP_200_OK)

class FilterStudentSubjectView(RetrieveAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, subject_name):

        if subject_name =='maths':
            queryset = StudentSubjectMath.objects.all()

            response_message={
                "students": queryset.values()
            }
            return Response(response_message, status=status.HTTP_200_OK)

        elif subject_name =='english':
            queryset = StudentSubjectEng.objects.all()

            response_message={
                "students": queryset.values()
            }
            return Response(response_message, status=status.HTTP_200_OK)

        raise exceptions.NotFound({
            "message": "Subject {subject} not Found".format(subject=subject_name) 
    })


class AssignStudentSubjectScoreView(UpdateAPIView):

    def put(self, request, reg_num):

        AddStudentSerializer.check_if_student_exists(reg_num)

        SubjectMathSerializer.update(regNum=reg_num, data=request.data)
        SubjectEngSerializer.update(regNum=reg_num, data=request.data)

        response_message={
            "message": "Successfully assigned scores to student {regNumber}".format(regNumber=reg_num)
        }

        return Response(response_message, status=status.HTTP_200_OK)
