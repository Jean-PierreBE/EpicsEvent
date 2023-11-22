# from django.contrib.auth.models import User
# from django.contrib.auth.models import User
from users_api.models import UserProfile
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

import pytest


@pytest.fixture
def superuser_client():
    user = UserProfile.objects.create_user(
        pseudo="john",
        first_name="toto",
        last_name="coucou",
        email="js@js.com",
        password="toto",
        role="GES",
    )
    user.is_admin = True
    user.is_staff = True
    user.save()
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    return client

@pytest.fixture
def gestionnaire_client():
    user = UserProfile.objects.create_user(
        pseudo="john",
        first_name="toto",
        last_name="coucou",
        email="js_ges@js.com",
        password="toto",
        role="GES",
    )
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    return client


@pytest.fixture
def commercial():
    user = UserProfile.objects.create_user(
        pseudo="john",
        first_name="toto",
        last_name="coucou",
        email="js_com@js.com",
        password="toto",
        role="COM",
    )
    return user


@pytest.fixture
def commercial_client(commercial):
    client = APIClient()
    refresh = RefreshToken.for_user(commercial)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    return client
