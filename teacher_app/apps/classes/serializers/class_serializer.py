from django.core import exceptions

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework import exceptions as rest_exception

from ..models import StudentClass
from ...authentication.models import User


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

    @staticmethod
    def check_if_teacher_is_owner(classname, teacher_id):
        class_teacher = StudentClass.objects.get(className=classname)
        if class_teacher.teacher.id != teacher_id:
            raise exceptions.PermissionDenied()
        return classname, teacher_id

    @staticmethod
    def check_if_class_exists(classname):
        try:
            searched_class = StudentClass.objects.get(className=classname)
        except StudentClass.DoesNotExist:
            raise rest_exception.NotFound({
                "message": "Class {classname} was not found".format(classname=classname)
            })
        return searched_class

    def create(self, data):
        new_class = StudentClass(**data)
        new_class.save()
        return new_class

    def update(self, instance, edited_data):
        for (key, value) in edited_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class ViewClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClass
        fields = '__all__'

    @staticmethod
    def retrieve_my_classes(request):
        my_classes = StudentClass.objects.all().filter(teacher=request.user.id)
        return my_classes.values('className', 'teacher')
