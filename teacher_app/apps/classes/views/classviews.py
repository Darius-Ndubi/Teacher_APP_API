from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView
)
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework.response import Response

from ..serializers import (
    ClassSerializer,
    ViewClassesSerializer
)

"""
    View to Create new Class
"""


class CreateClassView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ClassSerializer

    def post(self, request):

        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            ClassSerializer.check_if_user_is_teacher(request.user.id)
            serializer.save()

            response_message = {
                "message": "Successful added a new class"
            }

            return Response(response_message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
    View to List classes related to a teacher
"""


class ViewClasses(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ViewClassesSerializer

    def get(self, request):
        queryset = ViewClassesSerializer.retrieve_my_classes(request=request)

        response_message = {
            "data": queryset,
            "message": "These are your classes"
        }

        return Response(response_message, status=status.HTTP_200_OK)
