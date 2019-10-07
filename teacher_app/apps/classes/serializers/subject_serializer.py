from rest_framework import serializers

from ..models import (
    StudentSubjectMath,
    StudentSubjectEng
)


class SubjectMathSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField()

    class Meta:
        model = StudentSubjectMath
        fields = '__all__'

    def validate_math_field(subject_math):
        if subject_math == '':
            raise serializers.ValidationError({"message": "Kindly state with" +
                                              " True to assign, False to not " +
                                               "assign the subject to student",
                                               "Field": "maths"
                                               })
        return subject_math

    def create(self, data):
        new_student = StudentSubjectMath(**data)
        new_student.save()
        return new_student


class SubjectEngSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField()

    class Meta:
        model = StudentSubjectEng
        fields = '__all__'

    def validate_eng_field(subject_eng):
        if subject_eng == '':
            raise serializers.ValidationError({"message": "Kindly state with" +
                                              " True to assign, False to not" +
                                               " assign the subject to student",
                                               "Field": "english"
                                               })
        return subject_eng

    def create(self, data):
        new_student = StudentSubjectEng(**data)
        new_student.save()
        return new_student
