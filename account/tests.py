from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
import json
from django.contrib.auth.models import User


client = Client()


class CreateNewUserTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'username': 'sani',
            'email': 'sani@example.com',
            'password': 'absjsjjscd12'
        }
        self.invalid_payload = {
            'username': 'sani',
            'email': 'saniexample.com',
            'password': 'absjsjjscd12'
        }

    def test_create_valid_puppy(self):
        response = client.post(
            reverse('user_register'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response = client.post(
            reverse('user_register'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LoginAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='sani', email='sani@gmail.com', password='sani1234')
        self.valid_cred = {
            'username': 'sani',
            'password': 'sani1234'
        }
        self.invalid_cred = {
            'username': 'sani',
            'password': 'sani1234r'
        }

    def test_login_ok(self):
        response = client.post(
            reverse('user_login'),
            data=json.dumps(self.valid_cred),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_failed(self):
        response = client.post(
            reverse('user_login'),
            data=json.dumps(self.invalid_cred),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
