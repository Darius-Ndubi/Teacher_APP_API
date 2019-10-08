import json

from django.test import TestCase, Client

from rest_framework import status

from .test_add_student_class import TestAddstudentClass
from .test_view_subjects_student import TestViewStudentSubjects

login_response = TestAddstudentClass()
assing_subjects = TestViewStudentSubjects()


class TestStudentScoreAverage(TestCase):
    def setUp(self):
        self.client = Client()

    def assing_subjects_scores(self):
        login_resp = login_response.login_user()
        assing_subjects.assign_student_subject()
        client = Client()
        student_score = {"maths_score": 49, "english_score": 50}

        response = client.put(
            '/api/subjects/11111/score/',
            data=json.dumps(student_score),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        return response

    def test_student_score_average(self):
        self.assing_subjects_scores()
        login_resp = login_response.login_user()

        response = self.client.get(
            '/api/scores/student/11111/',
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
