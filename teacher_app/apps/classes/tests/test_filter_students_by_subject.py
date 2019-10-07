import json
from rest_framework import status
from django.test import TestCase,Client

from rest_framework.test import APIClient

from teacher_app.apps.classes.tests.test_add_student_class import TestAddstudentClass
from teacher_app.apps.classes.tests.test_view_subjects_student import TestViewStudentSubjects

login_response =  TestAddstudentClass()
assing_subjects = TestViewStudentSubjects()

class TestFilterStudentsSubjectView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_filter_students_by_subject_maths(self):
        login_resp = login_response.login_user()
        assing_subjects.assign_student_subject()

        response = self.client.get(
            '/api/subjects/maths/filter/',
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_students_by_subject_english(self):
        login_resp = login_response.login_user()
        assing_subjects.assign_student_subject()

        response = self.client.get(
            '/api/subjects/english/filter/',
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_students_by_unknown_subject(self):
        login_resp = login_response.login_user()
        assing_subjects.assign_student_subject()

        response = self.client.get(
            '/api/subjects/englddish/filter/',
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
