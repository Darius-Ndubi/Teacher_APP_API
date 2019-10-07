import json

from rest_framework import status
from django.urls import reverse
from django.test import TestCase,Client

from rest_framework.test import APIClient

from teacher_app.apps.classes.tests.test_add_student_class import TestAddstudentClass

add_student_inst = TestAddstudentClass()

class TestviewStudentsOfClass(TestCase):

    def setUp(self):
        self.client = Client()

    def add_student(self):
        add_student_inst.create_class()
        login_resp = add_student_inst.login_user()
        url = reverse('add_new_student')
        mock_student = {"firstName": "Denddnddis", "lastName": "Dennddoo","age": 25, "regNumber": "11111", "className": "1 west"}
        client = Client()
        response = client.post(
            url,
            data=json.dumps(mock_student),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        return response


    def test_retrieve_students_of_class(self):
        
        self.add_student()
        login_resp = add_student_inst.login_user()
        response =  self.client.get(
            '/api/students/class/1 west/',
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['data'][0].get('regNumber'), '11111')
        self.assertEqual(response.data['message'], 'These are students ofclass 1 west')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
