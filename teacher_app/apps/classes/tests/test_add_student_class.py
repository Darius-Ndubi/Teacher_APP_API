import json
from rest_framework import status
from django.urls import reverse
from django.test import TestCase,Client

from rest_framework.test import APIClient

from teacher_app.apps.authentication.tests.test_login import TestUserLogin

class TestAddstudentClass(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.url = reverse('add_new_student')
        self.mock_student = {"firstName": "Denddnddis", "lastName": "Dennddoo","age": 25, "regNumber": "11111", "className": "1 west"}

    def login_user(self):
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

    def create_class(self):
        url = reverse('add_new_class')
        login_resp=self.login_user()
        mock_add_class={"className": "1 west"}
        client = Client()
        response=client.post(
            url,
            data=json.dumps(mock_add_class),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        return response

    def test_add_student_class_no_firstName(self):
        login_resp=self.login_user()
        self.create_class()
        self.mock_student['firstName']=''
        response =  self.client.post(
            self.url,
            data=json.dumps(self.mock_student),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['firstName'][0],'This field may not be blank.')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_student_class_no_lastName(self):
        login_resp=self.login_user()
        self.create_class()
        self.mock_student['lastName']=''
        response =  self.client.post(
            self.url,
            data=json.dumps(self.mock_student),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['lastName'][0],'This field may not be blank.')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_student_class_string_age(self):
        login_resp=self.login_user()
        self.create_class()
        self.mock_student['age']= 'Null'
        response =  self.client.post(
            self.url,
            data=json.dumps(self.mock_student),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )

        self.assertEqual(response.data['age'][0],'A valid integer is required.')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_student_class_no_reg_num(self):
        login_resp=self.login_user()
        self.create_class()
        self.mock_student['regNumber']= ''
        response =  self.client.post(
            self.url,
            data=json.dumps(self.mock_student),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['regNumber'][0],'This field may not be blank.')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_add_student_class_not_exist(self):
        login_resp=self.login_user()
        response =  self.client.post(
            self.url,
            data=json.dumps(self.mock_student),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_student_sussessfully(self):
        login_resp=self.login_user()
        self.create_class()
        response =  self.client.post(
            self.url,
            data=json.dumps(self.mock_student),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + login_resp.data['access_token']
        )
        self.assertEqual(response.data['message'],'Successful added a new student')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)