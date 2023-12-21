import pytest
from rest_framework import status
from users_api.models import UserProfile
from django.shortcuts import get_object_or_404
from users_api.constants import PASSWORD_TEST


@pytest.mark.django_db
def test_super_user(superuser_client):
    data = {
        "pseudo": "test01",
        "first_name": "prenom01",
        "last_name": "nom01",
        "email": "nom01@mail.be",
        "role": "COM",
        "password": PASSWORD_TEST,
    }
    response = superuser_client.post("/signup/", data=data)
    response_dict = response.json()
    record = get_object_or_404(UserProfile, pk=response_dict["id"])
    assert response.status_code == status.HTTP_201_CREATED, response.content
    assert record.pseudo == "test01"
    assert record.first_name == "prenom01"
    assert record.last_name == "nom01"
    assert record.email == "nom01@mail.be"
    assert record.role == "COM"


@pytest.mark.django_db
def test_ges_user(ges_client):
    data = {
        "pseudo": "test02",
        "first_name": "prenom01",
        "last_name": "nom01",
        "email": "test02@mail.be",
        "role": "COM",
        "password": PASSWORD_TEST,
    }
    response = ges_client.post("/signup/", data=data)
    response_dict = response.json()
    record = get_object_or_404(UserProfile, pk=response_dict["id"])
    assert response.status_code == status.HTTP_201_CREATED, response.content
    assert record.pseudo == "test02"
    assert record.first_name == "prenom01"
    assert record.last_name == "nom01"
    assert record.email == "test02@mail.be"
    assert record.role == "COM"


@pytest.mark.django_db
def test_ges_com(com_client):
    data = {
        "pseudo": "test03",
        "first_name": "prenom01",
        "last_name": "nom01",
        "email": "test03@mail.be",
        "role": "COM",
        "password": PASSWORD_TEST,
    }
    response = com_client.post("/signup/", data=data)
    count = UserProfile.objects.filter(pseudo="test03").count()
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert count == 0


@pytest.mark.django_db
def test_ges_sup(sup_client):
    data = {
        "pseudo": "test04",
        "first_name": "prenom01",
        "last_name": "nom01",
        "email": "test04@mail.be",
        "role": "COM",
        "password": PASSWORD_TEST,
    }
    response = sup_client.post("/signup/", data=data)
    count = UserProfile.objects.filter(pseudo="test04").count()
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert count == 0
