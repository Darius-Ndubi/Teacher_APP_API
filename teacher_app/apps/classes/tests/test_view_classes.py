import json
from rest_framework import status
from django.urls import reverse
from django.test import TestCase,Client

from rest_framework.test import APIClient

from teacher_app.apps.classes.tests.test_add_student_class import TestAddstudentClass

add_student_inst = TestAddstudentClass()

class TestTeacherViewClasses(TestCase):
    def setUp(self):
        self.client = Client() 
        self.url = reverse('list_my_classes')

    def test_retrieve_teacher_classes(self):
        add_student_inst.create_class()
        login_resp = add_student_inst.login_user()
        response =  self.client.get(
            self.url,
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['data'][0].get('className'), '1 west')
        self.assertEqual(response.data['message'], 'These are your classes')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
