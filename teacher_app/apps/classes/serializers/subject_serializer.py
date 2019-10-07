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

    def validate_math_field(self, subject_math):
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

    @staticmethod
    def update(regNum, data):
        if data['maths_score'] is None or type(data['maths_score']) is not int:
            raise serializers.ValidationError({"message": "Kindly enter the maths score"})

        updated_math_score = StudentSubjectMath.objects.filter(student_reg_num=regNum).update(score=data['maths_score'])
        return updated_math_score


class SubjectEngSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField()

    class Meta:
        model = StudentSubjectEng
        fields = '__all__'

    def validate_eng_field(self, subject_eng):
        if subject_eng == '':
            raise serializers.ValidationError({"message": "Kindly state with" +
                                              " True to assign, False to not" +
                                               " assign the subject to student",
                                               "Field": "english"
                                               })
        return subject_eng

    @staticmethod
    def update(regNum, data):
        if data['english_score'] is None or type(data['english_score']) is not int:
            raise serializers.ValidationError({"message": "Kindly enter the english score"})

        updated_math_score = StudentSubjectEng.objects.filter(student_reg_num=regNum).update(score=data['english_score'])
        return updated_math_score

    def create(self, data):
        new_student = StudentSubjectEng(**data)
        new_student.save()
        return new_student
