import json
from rest_framework import status
from django.test import TestCase,Client

from rest_framework.test import APIClient

from teacher_app.apps.classes.tests.test_view_students_of_class import TestviewStudentsOfClass
from teacher_app.apps.classes.tests.test_add_student_class import TestAddstudentClass


add_student_inst = TestviewStudentsOfClass()
login_response =  TestAddstudentClass()

class TestEditStudentDetails(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.mock_edit_student = {"firstName": "Dennis", "lastName": "Dennddoo","age": 25, "regNumber": "121111", "className": "1 west"}


    def test_try_edit_wrong_regnum(self):
        add_student_inst.add_student()
        login_resp = login_response.login_user()

        response = self.client.put(
            '/api/students/343wqghdfd3245/edit',
            data=json.dumps(self.mock_edit_student),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['message'], 'Student with RegNo:343wqghdfd3245 was not found')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_try_edit_no_firstname(self):
        add_student_inst.add_student()
        login_resp = login_response.login_user()
        self.mock_edit_student['firstName'] = ""
        response = self.client.put(
            '/api/students/11111/edit',
            data=json.dumps(self.mock_edit_student),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['firstName'][0], 'This field may not be blank.')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_successfully_edit_student_info(self):
        add_student_inst.add_student()
        login_resp = login_response.login_user()

        response = self.client.put(
            '/api/students/11111/edit',
            data=json.dumps(self.mock_edit_student),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['message'], 'Student information was successfully updated')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
