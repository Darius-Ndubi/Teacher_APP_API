from django.test import TestCase, Client

from rest_framework import status

from .test_add_student_class import TestAddstudentClass
from .test_view_subjects_student import TestViewStudentSubjects
from .test_view_student_average_score import TestStudentScoreAverage

login_response = TestAddstudentClass()
assign_subjects = TestViewStudentSubjects()
assign_subject_score = TestStudentScoreAverage()


class TestClassScoreAverage(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_class_average(self):
        login_resp = login_response.login_user()
        assign_subjects.assign_student_subject()
        assign_subject_score.assing_subjects_scores()

        response = self.client.get(
            '/api/scores/class/1 west/',
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
