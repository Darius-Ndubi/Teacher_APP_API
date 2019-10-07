from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from rest_framework.response import Response

from teacher_app.apps.classes.serializers.student_serializers import (
    AddStudentSerializer,
    ViewStudentsSerializer
)
from teacher_app.apps.classes.serializers.class_serializer import (
    ClassSerializer
)

from teacher_app.apps.classes.models import StudentClass, Student

"""
    View to Add a new Student
"""


class AddStudentView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddStudentSerializer

    def post(self, request):
        students_class = get_object_or_404(
            StudentClass.objects.all(), className=request.data['className'])

        #  Assign The classname field to the retrieved id
        request.data['className'] = students_class.id

        serializer = self.serializer_class(
            data=request.data, context={'request': request}
        )
        # Check if the data is valid
        if serializer.is_valid():
            serializer.save()

            response_message = {
                "message": "Successful added a new student"
            }

            return Response(response_message, status=status.HTTP_201_CREATED)
        # Raise bad request error if data is wrong
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
    View to showstudents of a class
"""


class ViewStudentsOfClass(RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ViewStudentsSerializer

    def get(self, request, class_name):
        queryset = ViewStudentsSerializer.students_of_class(class_name)

        response_message = {
            "data": queryset,
            "message": "These are students of" +
            "class {classname}".format(classname=class_name)
        }
        return Response(response_message, status=status.HTTP_200_OK)


class EditStudentDetailView(UpdateAPIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, reg_num):

        student = AddStudentSerializer.check_if_student_exists(reg_num)

        class_name = ClassSerializer.check_if_class_exists(
            request.data['className'])

        request.data['className'] = class_name.id

        serializer = AddStudentSerializer(
            instance=student, data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()

            response_message = {
                "message": "Student information was successfully updated"
            }

            return Response(response_message, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchStudentView(RetrieveAPIView):

    permission_classes = [IsAuthenticated]

    def get (self, request, student_detail):

        searched_student = Student.objects.filter(
            Q(firstName__icontains=student_detail) | Q(lastName__icontains=student_detail) | Q(age__icontains=student_detail)
        )

        response_message = {
            "data": searched_student.values(),
            "message": "Student(s) information was successfully retrieved"
        }

        return Response(response_message, status=status.HTTP_200_OK)
