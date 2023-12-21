import pytest
from rest_framework import status
from users_api.models import UserProfile
from users_api.constants import PASSWORD_TEST


@pytest.mark.django_db
def test_role_error(ges_client):
    data = {
        "pseudo": "test02",
        "first_name": "prenom01",
        "last_name": "nom01",
        "email": "test02@mail.be",
        "role": "ad",
        "password": PASSWORD_TEST,
    }
    response = ges_client.post("/signup/", data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.content
    assert str(response.data["role"][0]) == '"ad" is not a valid choice.'


@pytest.mark.django_db
def test_create_same_user(ges_client):
    user_test = UserProfile(pseudo="test01",
                            first_name="prenom01",
                            last_name="nom01",
                            email="nom01@mail.be",
                            role="COM",
                            password=PASSWORD_TEST)
    user_test.save()
    data = {
        "pseudo": "test01",
        "first_name": "prenom02",
        "last_name": "nom02",
        "email": "nom02@mail.be",
        "role": "GES",
        "password": PASSWORD_TEST,
    }
    response = ges_client.post("/signup/", data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.content
    assert str(response.data["pseudo"][0]) == 'user profile with this pseudo already exists.'


@pytest.mark.django_db
def test_put_same_email(ges_client):
    user_test = UserProfile(pseudo="test01",
                            first_name="prenom01",
                            last_name="nom01",
                            email="nom01@mail.be",
                            role="SUP",
                            password=PASSWORD_TEST)
    user_test.save()
    data = {
        "pseudo": "test02",
        "first_name": "prenom02",
        "last_name": "nom02",
        "email": "nom01@mail.be",
        "role": "GES",
        "password": PASSWORD_TEST,
    }
    response = ges_client.post("/signup/", data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.content
    assert str(response.data["email"][0]) == 'user profile with this email already exists.'
