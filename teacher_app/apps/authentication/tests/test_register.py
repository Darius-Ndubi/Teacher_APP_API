import json
from rest_framework import status
from django.urls import reverse
from django.test import TestCase,Client

from rest_framework.test import APIClient

class TestUserRegistration(TestCase):

    def setUp(self):
        self.client = Client() 
        self.url = reverse('register') 
        self.mock_reg = {"firstName": "TestDarius","lastName": "TestNdubi","username": "TestTeacher","email": "testteacher@gmail.com","password": "2@Masese2023","is_teacher": "True"}

    def test_registration_no_firstname(self):
        self.mock_reg['firstName'] = ''
        response = self.client.post(
            self.url,
            data=json.dumps(self.mock_reg),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_no_lastname(self):
        self.mock_reg['lastName'] = ''
        response = self.client.post(
            self.url,
            data=json.dumps(self.mock_reg),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_no_username(self):
        self.mock_reg['username'] = ''
        response = self.client.post(
            self.url,
            data=json.dumps(self.mock_reg),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_no_email(self):
        self.mock_reg['email'] = ''
        response = self.client.post(
            self.url,
            data=json.dumps(self.mock_reg),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_email_wrong_format(self):
        self.mock_reg['email'] = 'testteachergmail.com'
        response = self.client.post(
            self.url,
            data=json.dumps(self.mock_reg),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_no_password(self):
        self.mock_reg['password'] = ''
        response = self.client.post(
            self.url,
            data=json.dumps(self.mock_reg),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_short_password(self):
        self.mock_reg['password'] = 'aaddcc'
        response = self.client.post(
            self.url,
            data=json.dumps(self.mock_reg),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_registration_weak_password(self):
        self.mock_reg['password'] = 'aaddccA2'
        response = self.client.post(
            self.url,
            data=json.dumps(self.mock_reg),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_successfull_registration(self):
        response =  self.client.post(
            self.url,
            data=json.dumps(self.mock_reg),
            content_type='application/json'
        )
        self.assertEqual(response.data['message'],"Registration was successfull proceed to login")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
