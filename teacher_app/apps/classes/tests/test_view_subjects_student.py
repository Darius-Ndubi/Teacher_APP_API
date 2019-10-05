import json
from rest_framework import status
from django.urls import reverse
from django.test import TestCase,Client

from rest_framework.test import APIClient

from teacher_app.apps.classes.tests.test_view_students_of_class import TestviewStudentsOfClass
from teacher_app.apps.classes.tests.test_add_student_class import TestAddstudentClass

add_student_inst = TestviewStudentsOfClass()
login_response =  TestAddstudentClass()

class TestViewStudentSubjects(TestCase):

    def setUp(self):
        self.client = Client()

    def assign_student_subject(self):
        add_student_inst.add_student()
        login_resp = login_response.login_user()
        subject_data = {"regNumber": "11111","maths": "True","english": "False"}
        url = reverse("give_student_subject")

        response = self.client.post(
            url,
            data=json.dumps(subject_data),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        return response

    def test_get_student_subject_data(self):
        self.assign_student_subject()
        login_resp = login_response.login_user()
        response = self.client.get(
            '/api/subjects/11111/',
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
