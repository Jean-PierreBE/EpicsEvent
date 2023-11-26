import pytest
from rest_framework import status


# Version simple
@pytest.mark.django_db
def test_contract_create_ok_com(commercial_client):
    """Create contract ok, role GES"""
    data = {
        "enterprise_name": "BELGACOM",
        "client_name": "moi",
        "information": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum interdum ",
        "email": "stein01@mail.be",
        "phone": "+32486303558"
    }
    response = commercial_client.post("/customers/", data=data)
    assert response.status_code == status.HTTP_201_CREATED, response.content


@pytest.mark.django_db
def test_contract_create_nok_ges(gestionnaire_client):
    """Create contract nok, role COM"""
    data = {
        "enterprise_name": "BELGACOM",
        "client_name": "moi",
        "information": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum interdum ",
        "email": "stein01@mail.be",
        "phone": "+32486303558"
    }
    response = gestionnaire_client.post("/customers/", data=data)
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content


@pytest.mark.django_db
def test_contract_create_nok_sup(support_client):
    """Create contract nok, role COM"""
    data = {
        "enterprise_name": "BELGACOM",
        "client_name": "moi",
        "information": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum interdum ",
        "email": "stein01@mail.be",
        "phone": "+32486303558"
    }
    response = support_client.post("/customers/", data=data)
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
