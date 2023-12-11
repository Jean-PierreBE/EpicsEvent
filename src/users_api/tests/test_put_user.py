import pytest
from rest_framework import status
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
        "first_name": "prenom01",
        "last_name": "nom01",
        "email": "nom01@mail.be",
        "role": "GES",
        "password": "Ulysse1786",
    }
    response = superuser_client.put(f"/signup/{user_test.id}/", data=data)
    assert response.status_code == status.HTTP_200_OK, response.content


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
        "first_name": "prenom01",
        "last_name": "nom01",
        "email": "nom01@mail.be",
        "role": "GES",
        "password": "Ulysse1786",
    }
    response = ges_client.put(f"/signup/{user_test.id}/", data=data)
    assert response.status_code == status.HTTP_200_OK, response.content
