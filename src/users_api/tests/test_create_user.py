import pytest
from rest_framework import status


# Version simple
@pytest.mark.django_db
def test_super_user(superuser_client):
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


@pytest.mark.django_db
def test_ges_user(ges_client):
    data = {
        "pseudo": "test02",
        "first_name": "prenom01",
        "last_name": "nom01",
        "email": "test02@mail.be",
        "role": "COM",
        "password": "Ulysse1786",
    }
    response = ges_client.post("/signup/", data=data)
    assert response.status_code == status.HTTP_201_CREATED, response.content


@pytest.mark.django_db
def test_ges_com(com_client):
    data = {
        "pseudo": "test03",
        "first_name": "prenom01",
        "last_name": "nom01",
        "email": "test03@mail.be",
        "role": "COM",
        "password": "Ulysse1786",
    }
    response = com_client.post("/signup/", data=data)
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content


@pytest.mark.django_db
def test_ges_sup(sup_client):
    data = {
        "pseudo": "test04",
        "first_name": "prenom01",
        "last_name": "nom01",
        "email": "test04@mail.be",
        "role": "COM",
        "password": "Ulysse1786",
    }
    response = sup_client.post("/signup/", data=data)
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content