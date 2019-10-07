import json
from rest_framework import status
from django.urls import reverse
from django.test import TestCase,Client

from rest_framework.test import APIClient


class TestUserLogin(TestCase):

    def setUp(self):
        self.client = Client() 
        self.url = reverse('login') 
        self.mock_log =  {"email": "testteacher@gmail.com","password": "2@Masese2023"}

    @staticmethod
    def register_user():
        mock_reg = {"firstName": "TestDarius","lastName": "TestNdubi","username": "TestTeacher","email": "testteacher@gmail.com","password": "2@Masese2023","is_teacher": "True"}
        url = reverse('register')
        client = Client()
        response = client.post(
            url,
            data=json.dumps(mock_reg),
            content_type='application/json'
        )
        return response

    def test_login_no_email(self):
        self.register_user()
        self.mock_log['email'] = ''
        response =  self.client.post(
            self.url,
            data=json.dumps(self.mock_log),
            content_type='application/json'
        )
        self.assertEqual(response.data['email'][0],'This field may not be blank.')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_no_password(self):
        self.register_user()
        self.mock_log['password'] = ''
        response =  self.client.post(
            self.url,
            data=json.dumps(self.mock_log),
            content_type='application/json'
        )
        self.assertEqual(response.data['password'][0],'This field may not be blank.')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_successfull_login(self):
        self.register_user()
        response =  self.client.post(
            self.url,
            data=json.dumps(self.mock_log),
            content_type='application/json'
        )
        self.assertEqual(response.data['message'],'Login was successful')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
