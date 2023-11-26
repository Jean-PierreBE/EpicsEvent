import pytest
from rest_framework import status
from events.models import Customer


# Version simple
@pytest.mark.django_db
def test_contract_put_ok_com(commercial, commercial_client):
    """Create contract ok, role GES"""
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    data = {
        "enterprise_name": "BELGACOM",
        "client_name": "moi",
        "information": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum interdum ",
        "email": "stein01@mail.be",
        "phone": "+32486303558"
    }
    response = commercial_client.put(f"/customers/{customer.id}/", data=data)
    assert response.status_code == status.HTTP_200_OK, response.content


@pytest.mark.django_db
def test_contract_put_nok_ges(commercial, gestionnaire_client):
    """Create contract nok, role COM"""
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    data = {
        "enterprise_name": "BELGACOM",
        "client_name": "moi",
        "information": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum interdum ",
        "email": "stein01@mail.be",
        "phone": "+32486303558"
    }
    response = gestionnaire_client.put(f"/customers/{customer.id}/", data=data)
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content


@pytest.mark.django_db
def test_contract_put_nok_sup(commercial, support_client):
    """Create contract nok, role COM"""
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    data = {
        "enterprise_name": "BELGACOM",
        "client_name": "moi",
        "information": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum interdum ",
        "email": "stein01@mail.be",
        "phone": "+32486303558"
    }
    response = support_client.put(f"/customers/{customer.id}/", data=data)
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
