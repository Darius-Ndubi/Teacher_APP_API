import json

from django.test import TestCase, Client

from rest_framework import status

from teacher_app.apps.classes.tests.test_add_student_class import TestAddstudentClass
from teacher_app.apps.classes.tests.test_view_subjects_student import TestViewStudentSubjects

login_response = TestAddstudentClass()
assing_subjects = TestViewStudentSubjects()


class TestAssignScoreStudent(TestCase):
    def setUp(self):
        self.client = Client()
        self.student_score = {"maths_score": 49,"english_score": 50}

    def test_student_assign_score_no_math(self):
        login_resp = login_response.login_user()
        assing_subjects.assign_student_subject()
        self.student_score['maths_score'] = ""
        response = self.client.put(
            '/api/subjects/11111/score/',
            data=json.dumps(self.student_score),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['message'], 'Kindly enter the maths score')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_student_assign_score_no_english(self):
        login_resp = login_response.login_user()
        assing_subjects.assign_student_subject()
        self.student_score['english_score'] = ""
        response = self.client.put(
            '/api/subjects/11111/score/',
            data=json.dumps(self.student_score),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['message'], 'Kindly enter the english score')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_student_assign_score(self):
        login_resp = login_response.login_user()
        assing_subjects.assign_student_subject()

        response = self.client.put(
            '/api/subjects/11111/score/',
            data=json.dumps(self.student_score),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['message'], 'Successfully assigned scores to student 11111')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
