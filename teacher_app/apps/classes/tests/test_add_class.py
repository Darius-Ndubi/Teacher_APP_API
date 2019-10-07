import json
from rest_framework import status
from django.urls import reverse
from django.test import TestCase,Client

from rest_framework.test import APIClient

from teacher_app.apps.authentication.tests.test_login import TestUserLogin

class TestTeacherAddClass(TestCase):

    def setUp(self):
        self.client = Client() 
        self.url = reverse('add_new_class')
        self.mock_add_class={"className": "1 west"}

    @staticmethod
    def login_user():
        TestUserLogin.register_user()
        mock_log =  {"email": "testteacher@gmail.com","password": "2@Masese2023"}
        url = reverse('login')
        client = Client()
        response =  client.post(
            url,
            data=json.dumps(mock_log),
            content_type='application/json'
        )
        return response

    def test_class_creation_no_token(self):
        self.mock_add_class['className'] = ''
        response =  self.client.post(
            self.url,
            data=json.dumps(self.mock_add_class),
            content_type='application/json'
        )
        self.assertEqual(response.data['detail'],'Authentication credentials were not provided.')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_class_creation_no_classname(self):
        login_resp=self.login_user()
        self.mock_add_class['className'] = ''
        response =  self.client.post(
            self.url,
            data=json.dumps(self.mock_add_class),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['className'][0],'This field may not be blank.')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_successfull_class_creation(self):
        login_resp=self.login_user()

        response =  self.client.post(
            self.url,
            data=json.dumps(self.mock_add_class),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['message'],'Successful added a new class')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_repeated_class_creation(self):
        login_resp=self.login_user()

        self.client.post(
            self.url,
            data=json.dumps(self.mock_add_class),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        response=self.client.post(
            self.url,
            data=json.dumps(self.mock_add_class),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['className'][0],'The classname Should be unique, Receiving this error means the class already exists')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
