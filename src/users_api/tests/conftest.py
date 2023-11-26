from users_api.models import UserProfile
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

import pytest


@pytest.fixture
def superuser_client():
    user = UserProfile.objects.create_user(
        pseudo="super",
        first_name="toto",
        last_name="coucou",
        email="super@js.com",
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
def ges_client():
    user = UserProfile.objects.create_user(
        pseudo="com",
        first_name="toto",
        last_name="coucou",
        email="ges@js.com",
        password="toto",
        role="GES",
    )
    user.is_admin = False
    user.is_staff = False
    user.save()
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    return client


@pytest.fixture
def com_client():
    user = UserProfile.objects.create_user(
        pseudo="com",
        first_name="toto",
        last_name="coucou",
        email="com@js.com",
        password="toto",
        role="COM",
    )
    user.is_admin = False
    user.is_staff = False
    user.save()
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    return client


@pytest.fixture
def sup_client():
    user = UserProfile.objects.create_user(
        pseudo="com",
        first_name="toto",
        last_name="coucou",
        email="com@js.com",
        password="toto",
        role="SUP",
    )
    user.is_admin = False
    user.is_staff = False
    user.save()
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    return client
