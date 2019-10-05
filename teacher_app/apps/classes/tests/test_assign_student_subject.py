import json
from rest_framework import status
from django.urls import reverse
from django.test import TestCase,Client

from rest_framework.test import APIClient

from teacher_app.apps.classes.tests.test_view_students_of_class import TestviewStudentsOfClass
from teacher_app.apps.classes.tests.test_add_student_class import TestAddstudentClass


add_student_inst = TestviewStudentsOfClass()
login_response =  TestAddstudentClass()

class TestAssignStudentSubject(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("give_student_subject")
        self.subject_data ={"regNumber": "11111","maths": "True","english": "True"}

    def test_assign_student_subject_wrong_regnumber(self):
        add_student_inst.add_student()
        login_resp = login_response.login_user()
        self.subject_data['regNumber'] = "123456w4"
        response = self.client.post(
            self.url,
            data=json.dumps(self.subject_data),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['message'], 'Student with RegNo:123456w4 was not found')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_assign_student_subject_no_math_subject(self):
        add_student_inst.add_student()
        login_resp = login_response.login_user()
        self.subject_data['maths'] = ""
        response = self.client.post(
            self.url,
            data=json.dumps(self.subject_data),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['message'], 'Kindly state with True to assign, False to not assign the subject to student')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_assign_student_subject_no_english_subject(self):
        add_student_inst.add_student()
        login_resp = login_response.login_user()
        self.subject_data['english'] = ""
        response = self.client.post(
            self.url,
            data=json.dumps(self.subject_data),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['message'], 'Kindly state with True to assign, False to not assign the subject to student')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_assign_student_subject_success(self):
        add_student_inst.add_student()
        login_resp = login_response.login_user()
        response = self.client.post(
            self.url,
            data=json.dumps(self.subject_data),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )

        self.assertEqual(response.data['message'], 'You have successfully assigned 11111 to 2 subjects')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
