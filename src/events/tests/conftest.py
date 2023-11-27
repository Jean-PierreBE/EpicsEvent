from users_api.models import UserProfile
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
import pytest


@pytest.fixture
def gestionnaire():
    user = UserProfile.objects.create_user(
        pseudo="ges01",
        first_name="toto",
        last_name="coucou",
        email="ges01@js.com",
        password="toto",
        role="GES",
    )

    return user

@pytest.fixture
def gestionnaire_client(gestionnaire):
    client = APIClient()
    refresh = RefreshToken.for_user(gestionnaire)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return client


@pytest.fixture
def commercial():
    user = UserProfile.objects.create_user(
        pseudo="com01",
        first_name="toto",
        last_name="coucou",
        email="com01@js.com",
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


@pytest.fixture
def commercial01_client():
    user = UserProfile.objects.create_user(
        pseudo="com02",
        first_name="toto",
        last_name="coucou",
        email="com021@js.com",
        password="toto",
        role="COM",
    )
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    return client


@pytest.fixture
def support():
    user = UserProfile.objects.create_user(
        pseudo="sup01",
        first_name="toto",
        last_name="coucou",
        email="sup01@js.com",
        password="toto",
        role="SUP",
    )

    return user


@pytest.fixture
def support_client(support):
    client = APIClient()
    refresh = RefreshToken.for_user(support)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    return client
