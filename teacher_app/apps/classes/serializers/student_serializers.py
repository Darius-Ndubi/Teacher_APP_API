from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework import exceptions as rest_exception

from ..models import StudentClass, Student


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
    className = serializers.PrimaryKeyRelatedField(
        queryset=StudentClass.objects.all())

    class Meta:
        model = Student
        fields = ['firstName', 'lastName', 'age', 'regNumber', 'className']

    @staticmethod
    def check_if_student_exists(regNum):
        try:
            searched_student = Student.objects.all().get(regNumber=regNum)
        except Student.DoesNotExist:
            raise rest_exception.NotFound({
                "message": "Student with RegNo:{regNumber} was not found".format(regNumber=regNum)
            })
        return searched_student

    def create(self, data):
        new_student = Student(**data)
        new_student.save()
        return new_student

    def update(self, instance, edited_student_data):
        for (key, value) in edited_student_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class ViewStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    @staticmethod
    def students_of_class(class_name):
        class_id = StudentClass.objects.get(className=class_name)
        all_students = Student.objects.all().filter(className=class_id.id)
        return all_students.values('firstName', 'lastName', 'age', 'regNumber')
