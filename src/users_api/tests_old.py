from django.urls import reverse
import pytest

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from users_api.models import UserProfile


class RegisterTestCase(APITestCase):
    token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAxODkxNzIzLC' \
            'JpYXQiOjE2OTkyOTk3MjMsImp0aSI6IjRkOGJlNmI2ZDkzZTQ0N2U5OTAxZDM4NzNhMjE5MWY3IiwidXNlcl9pZCI6MX0.T9MvY' \
            '6h74c1Zu3BapCfBES5gdHIKhrNjLLZjzW1TV1g'
    user = 'superuser'
    def test_register(self):
        data = { "pseudo": "test01",
                "first_name": "prenom01",
                "last_name": "nom01",
                "email": "nom01@mail.be",
                "role": "COM",
                "password": "Ulysse1786"}
        UserProfile.objects.create(
            pseudo=data.get('pseudo'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            role=data.get('role'),
            password=data.get('password')
        )
        response = self.client.post('/signup/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

