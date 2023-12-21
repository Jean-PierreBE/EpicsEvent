import pytest
from rest_framework import status
from django.shortcuts import get_object_or_404
from users_api.models import UserProfile


@pytest.mark.django_db
def test_put_super_user(superuser_client):
    user_test = UserProfile(pseudo="test01",
                            first_name="prenom01",
                            last_name="nom01",
                            email="nom01@mail.be",
                            role="COM",
                            password="Ulysse1786")
    user_test.save()
    data = {
        "pseudo": "test01",
        "first_name": "prenom02",
        "last_name": "nom02",
        "email": "nom02@mail.be",
        "role": "GES",
        "password": "Ulysse1786",
    }
    response = superuser_client.put(f"/signup/{user_test.id}/", data=data)
    record = get_object_or_404(UserProfile, pk=user_test.id)
    assert response.status_code == status.HTTP_200_OK, response.content
    assert record.pseudo == "test01"
    assert record.first_name == "prenom02"
    assert record.last_name == "nom02"
    assert record.email == "nom02@mail.be"
    assert record.role == "GES"


@pytest.mark.django_db
def test_put_ges_user(ges_client):
    user_test = UserProfile(pseudo="test01",
                            first_name="prenom01",
                            last_name="nom01",
                            email="nom01@mail.be",
                            role="COM",
                            password="Ulysse1786")
    user_test.save()
    data = {
        "pseudo": "test01",
        "first_name": "prenom02",
        "last_name": "nom02",
        "email": "nom02@mail.be",
        "role": "GES",
        "password": "Ulysse1786",
    }
    response = ges_client.put(f"/signup/{user_test.id}/", data=data)
    record = get_object_or_404(UserProfile, pk=user_test.id)
    assert response.status_code == status.HTTP_200_OK, response.content
    assert record.pseudo == "test01"
    assert record.first_name == "prenom02"
    assert record.last_name == "nom02"
    assert record.email == "nom02@mail.be"
    assert record.role == "GES"


@pytest.mark.django_db
def test_put_com_user(com_client):
    user_test = UserProfile(pseudo="test01",
                            first_name="prenom01",
                            last_name="nom01",
                            email="nom01@mail.be",
                            role="COM",
                            password="Ulysse1786")
    user_test.save()
    data = {
        "pseudo": "test01",
        "first_name": "prenom02",
        "last_name": "nom02",
        "email": "nom02@mail.be",
        "role": "GES",
        "password": "Ulysse1786",
    }
    response = com_client.put(f"/signup/{user_test.id}/", data=data)
    record = get_object_or_404(UserProfile, pk=user_test.id)
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert record.pseudo == "test01"
    assert record.first_name == "prenom01"
    assert record.last_name == "nom01"
    assert record.email == "nom01@mail.be"
    assert record.role == "COM"


@pytest.mark.django_db
def test_put_sup_user(sup_client):
    user_test = UserProfile(pseudo="test01",
                            first_name="prenom01",
                            last_name="nom01",
                            email="nom01@mail.be",
                            role="COM",
                            password="Ulysse1786")
    user_test.save()
    data = {
        "pseudo": "test01",
        "first_name": "prenom01",
        "last_name": "nom01",
        "email": "nom01@mail.be",
        "role": "GES",
        "password": "Ulysse1786",
    }
    response = sup_client.put(f"/signup/{user_test.id}/", data=data)
    record = get_object_or_404(UserProfile, pk=user_test.id)
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert record.pseudo == "test01"
    assert record.first_name == "prenom01"
    assert record.last_name == "nom01"
    assert record.email == "nom01@mail.be"
    assert record.role == "COM"
