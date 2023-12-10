import pytest
from rest_framework import status
from users_api.models import UserProfile
from users_api.constants import PASSWORD_TEST

@pytest.mark.django_db
def test_login(user_lambda, user_lambda_client):
    data = {
        "pseudo": user_lambda.pseudo,
        "password": PASSWORD_TEST
    }
    response =  user_lambda_client.post("/login/", data=data)
    assert response.status_code == status.HTTP_200_OK, response.content


@pytest.mark.django_db
def test_refresh(user_lambda, user_lambda_client):
    data = {
        "pseudo": user_lambda.pseudo,
        "password": PASSWORD_TEST
    }
    response = user_lambda_client.post("/login/", data=data)
    json_ret = response.json()
    data = {
        "refresh": json_ret['refresh']
    }
    response = user_lambda_client.post("/login/refresh/", data=data)
    assert response.status_code == status.HTTP_200_OK, response.content
