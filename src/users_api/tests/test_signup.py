from django.urls import reverse
import pytest

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from users_api.models import UserProfile


# Version simple
@pytest.mark.django_db
def test_register(superuser_client):
    data = {
        "pseudo": "test01",
        "first_name": "prenom01",
        "last_name": "nom01",
        "email": "nom01@mail.be",
        "role": "COM",
        "password": "Ulysse1786",
    }
    response = superuser_client.post("/signup/", data=data)
    assert response.status_code == status.HTTP_201_CREATED, response.content
