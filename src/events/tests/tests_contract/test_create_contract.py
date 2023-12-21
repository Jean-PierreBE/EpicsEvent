import pytest
from rest_framework import status
import datetime
from django.shortcuts import get_object_or_404
from events.models import Customer, Contract


# Version simple
@pytest.mark.django_db
def test_contract_create_ok_ges(commercial, gestionnaire_client):
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    data = {
        "sign_date": "2023-10-31",
        "amount_contract": "20000",
        "saldo_contract": "3000",
        "status_contract": "SI",
    }
    response = gestionnaire_client.post(f"/customers/{customer.id}/contracts/", data=data)
    response_dict = response.json()
    record = get_object_or_404(Contract, pk=response_dict["id"])
    assert response.status_code == status.HTTP_201_CREATED, response.content
    assert record.sign_date == datetime.date(2023, 10, 31)
    assert record.amount_contract == 20000.0
    assert record.saldo_contract == 3000.0
    assert record.status_contract == "SI"


@pytest.mark.django_db
def test_contract_create_nok_com(commercial, commercial_client):
    """Create contract nok, role COM"""
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    data = {
        "sign_date": "2023-10-31",
        "amount_contract": "20000",
        "saldo_contract": "3000",
        "status_contract": "SI",
    }
    response = commercial_client.post(f"/customers/{customer.id}/contracts/", data=data)
    count = Contract.objects.filter(customer_id=customer.id).count()
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert count == 0


@pytest.mark.django_db
def test_contract_create_nok_sup(commercial, support_client):
    """Create contract nok, role COM"""
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    data = {
        "sign_date": "2023-10-31",
        "amount_contract": "20000",
        "saldo_contract": "3000",
        "status_contract": "SI",
    }
    response = support_client.post(f"/customers/{customer.id}/contracts/", data=data)
    count = Contract.objects.filter(customer_id=customer.id).count()
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert count == 0
