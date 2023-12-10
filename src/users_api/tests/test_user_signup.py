import pytest
from rest_framework import status
from users_api.models import UserProfile
from users_api.constants import PASSWORD_TEST


@pytest.mark.django_db
def test_signup_one_user(superuser_client):
    user_test = UserProfile(pseudo="test01",
                            first_name="prenom01",
                            last_name="nom01",
                            email="nom01@mail.be",
                            role="COM",
                            password=PASSWORD_TEST)
    user_test.save()
    response = superuser_client.get(f"/signup/{user_test.id}/")
    assert response.status_code == status.HTTP_200_OK, response.content


@pytest.mark.django_db
def test_signup_all_user(superuser_client):
    user_test = UserProfile(pseudo="test01",
                            first_name="prenom01",
                            last_name="nom01",
                            email="nom01@mail.be",
                            role="COM",
                            password=PASSWORD_TEST)
    user_test.save()
    response = superuser_client.get("/signup/")
    assert response.status_code == status.HTTP_200_OK, response.content
