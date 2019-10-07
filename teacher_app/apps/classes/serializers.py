from django.core import exceptions

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import StudentClass, Student
from ..authentication.models import User


class ClassSerializer(serializers.ModelSerializer):
    className = serializers.CharField(required=True, validators={
        UniqueValidator(
            queryset=StudentClass.objects.all(),
            message=(
                "The classname Should be unique, Receiving this error" +
                " means the class already exists"
            )
        )
    })
    teacher = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = StudentClass
        fields = '__all__'

    @staticmethod
    def check_if_user_is_teacher(data):
        user_teacher = User.objects.get(id=data)
        if user_teacher.is_teacher is False:
            raise exceptions.PermissionDenied()
        return data

    def create(self, data):
        new_class = StudentClass(**data)
        new_class.save()
        return new_class


class ViewClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClass
        fields = '__all__'

    @staticmethod
    def retrieve_my_classes(request):
        my_classes = StudentClass.objects.all().filter(teacher=request.user.id)
        return my_classes.values('className', 'teacher')


class AddStudentSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(required=True)
    lastName = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    regNumber = serializers.CharField(required=True, validators={
        UniqueValidator(
            queryset=Student.objects.all(),
            message=(
                "Student's registration number should be unique"
            )
        )
    })
    className = serializers.PrimaryKeyRelatedField(queryset=StudentClass.objects.all())

    class Meta:
        model = Student
        fields = ['firstName', 'lastName', 'age', 'regNumber', 'className']

    def create(self, data):
        new_student = Student(**data)
        new_student.save()
        return new_student


class ViewStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    @staticmethod
    def students_of_class(class_name):
        class_id = StudentClass.objects.get(className=class_name)
        all_students = Student.objects.all().filter(className=class_id.id)
        return all_students.values('firstName', 'lastName', 'age', 'regNumber')
