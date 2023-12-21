import pytest
from rest_framework import status
from django.shortcuts import get_object_or_404
from events.models import Customer


# Version simple
@pytest.mark.django_db
def test_contract_put_ok_com(commercial, commercial_client):
    """Create contract ok, role GES"""
    customer = Customer(enterprise_name='PROXIMUS',
                        client_name='toujours moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein01@mail.be',
                        phone='+32486303568',
                        author_user=commercial)
    customer.save()
    data = {
        "enterprise_name": "BELGACOM",
        "client_name": "moi",
        "information": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum interdum",
        "email": "stein01@mail.be",
        "phone": "+32486303558"
    }
    response = commercial_client.put(f"/customers/{customer.id}/", data=data)
    record = get_object_or_404(Customer, pk=customer.id)
    assert response.status_code == status.HTTP_200_OK, response.content
    assert record.enterprise_name == "BELGACOM"
    assert record.client_name == "moi"
    assert record.information == "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum interdum"
    assert record.email == "stein01@mail.be"
    assert record.phone == "+32486303558"


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
        "enterprise_name": "BELGACOM1",
        "client_name": "moi encore",
        "information": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum interdum ",
        "email": "stein02@mail.be",
        "phone": "+32486303559"
    }
    response = gestionnaire_client.put(f"/customers/{customer.id}/", data=data)
    record = get_object_or_404(Customer, pk=customer.id)
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert record.enterprise_name == "BELGACOM"
    assert record.client_name == "moi"
    assert record.information == "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean "
    assert record.email == "stein@mail.be"
    assert record.phone == "+32486303558"


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
        "enterprise_name": "PROXIMUS",
        "client_name": "moi",
        "information": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum interdum ",
        "email": "stein02@mail.be",
        "phone": "+32486303559"
    }
    response = support_client.put(f"/customers/{customer.id}/", data=data)
    record = get_object_or_404(Customer, pk=customer.id)
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert record.enterprise_name == "BELGACOM"
    assert record.client_name == "moi"
    assert record.information == "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean "
    assert record.email == "stein@mail.be"
    assert record.phone == "+32486303558"
