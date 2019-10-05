from django.db import models


from teacher_app.apps.authentication.models import User

"""
    Model on class data
"""


class StudentClass(models.Model):
    className = models.CharField("Name of the class", null=False,
                                 max_length=254, unique=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)


"""
    Model on Student data
"""


class Student(models.Model):
    firstName = models.CharField("Students's first name",
                                 max_length=50,
                                 null=False)
    lastName = models.CharField("Students's last name", max_length=50,
                                null=False)
    age = models.IntegerField(null=False)
    regNumber = models.CharField("Students registration number",
                                 max_length=50, unique=True)
    className = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
