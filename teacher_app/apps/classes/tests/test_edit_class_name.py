import json
from rest_framework import status
from django.test import TestCase, Client


from teacher_app.apps.classes.tests.test_add_student_class import TestAddstudentClass

add_student_inst = TestAddstudentClass()

class TestTeacherEditClass(TestCase):
    def setUp(self):
        self.client = Client()
        self.mock_edit_class = {"className": "2 west"}

    def test_edit_class_teacher_no_class_info(self):
        add_student_inst.create_class()
        login_resp = add_student_inst.login_user()
        self.mock_edit_class['className'] = ""
        response =  self.client.put(
            '/api/classes/1 west/edit',
            data=json.dumps( self.mock_edit_class),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['className'][0], 'This field may not be blank.')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_edit_non_existent_class(self):
        add_student_inst.create_class()
        login_resp = add_student_inst.login_user()
        response =  self.client.put(
            '/api/classes/1 wedst/edit',
            data=json.dumps( self.mock_edit_class),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )

        self.assertEqual(response.data['message'], 'Class 1 wedst was not found')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_edit_class_teacher(self):
        add_student_inst.create_class()
        login_resp = add_student_inst.login_user()

        response =  self.client.put(
            '/api/classes/1 west/edit',
            data=json.dumps( self.mock_edit_class),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['message'], 'Updated class name from 1 west to 2 west')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
