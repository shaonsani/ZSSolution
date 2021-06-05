from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
import json

client = Client()

class CreateNewUserTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'username':'sani',
            'email':'sani@example.com',
            'password':'absjsjjscd12'
        }
        self.invalid_payload = {
            'username':'sani',
            'email':'saniexample.com',
            'password':'absjsjjscd12'
        }

    def test_create_valid_puppy(self):
        response = client.post(
            reverse('use_register'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response = client.post(
            reverse('use_register'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
