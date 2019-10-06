from rest_framework import status
from django.test import TestCase,Client

from rest_framework.test import APIClient

from teacher_app.apps.classes.tests.test_add_student_class import TestAddstudentClass
from teacher_app.apps.classes.tests.test_view_students_of_class import TestviewStudentsOfClass

add_student_inst = TestAddstudentClass()
create_student = TestviewStudentsOfClass()

class TestSearchStudent(TestCase):
    def setUp(self):
        self.client = Client()

    def test_search_student(self):
        login_resp = add_student_inst.login_user()
        create_student.add_student()

        response = self.client.get(
            '/api/students/denn/search/',
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['message'], 'Student(s) information was successfully retrieved')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
