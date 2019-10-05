from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from rest_framework.response import Response

from ..serializers import (
    AddStudentSerializer,
    ViewStudentsSerializer
)
from ..models import StudentClass

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
