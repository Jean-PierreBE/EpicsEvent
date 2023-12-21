import pytest
import datetime
from rest_framework import status
from django.shortcuts import get_object_or_404
from events.models import Customer, Contract


@pytest.mark.django_db
def test_contract_put_ok_ges(commercial, gestionnaire, gestionnaire_client):
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    contract = Contract(customer_id=customer.id,
                        sign_date="2023-12-21",
                        amount_contract=10000,
                        saldo_contract=5000,
                        status_contract="NS",
                        author_user=gestionnaire)
    contract.save()
    data = {
        "sign_date": "2023-11-30",
        "amount_contract": "50000",
        "saldo_contract": "4000",
        "status_contract": "NS",
    }
    response = gestionnaire_client.put(f"/customers/{customer.id}/contracts/{contract.id}/", data=data)
    record = get_object_or_404(Contract, pk=contract.id)
    assert response.status_code == status.HTTP_200_OK, response.content
    assert record.sign_date == datetime.date(2023, 11, 30)
    assert record.amount_contract == 50000.0
    assert record.saldo_contract == 4000.0
    assert record.status_contract == "NS"


@pytest.mark.django_db
def test_contract_put_ok_same_com(commercial, gestionnaire, commercial_client):
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    contract = Contract(customer_id=customer.id,
                        sign_date="2023-12-21",
                        amount_contract=10000,
                        saldo_contract=5000,
                        status_contract="NS",
                        author_user=gestionnaire)
    contract.save()
    data = {
        "sign_date": "2023-11-30",
        "amount_contract": "50000",
        "saldo_contract": "4000",
        "status_contract": "NS",
    }
    response = commercial_client.put(f"/customers/{customer.id}/contracts/{contract.id}/", data=data)
    record = get_object_or_404(Contract, pk=contract.id)
    assert response.status_code == status.HTTP_200_OK, response.content
    assert record.sign_date == datetime.date(2023, 11, 30)
    assert record.amount_contract == 50000.0
    assert record.saldo_contract == 4000.0
    assert record.status_contract == "NS"


@pytest.mark.django_db
def test_contract_put_nok_diff_com(commercial, gestionnaire, commercial01_client):
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    contract = Contract(customer_id=customer.id,
                        sign_date="2023-12-21",
                        amount_contract=10000,
                        saldo_contract=5000,
                        status_contract="NS",
                        author_user=gestionnaire)
    contract.save()
    data = {
        "sign_date": "2023-11-30",
        "amount_contract": "50000",
        "saldo_contract": "4000",
        "status_contract": "NS",
    }
    response = commercial01_client.put(f"/customers/{customer.id}/contracts/{contract.id}/", data=data)
    record = get_object_or_404(Contract, pk=contract.id)
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert record.sign_date == datetime.date(2023, 12, 21)
    assert record.amount_contract == 10000.0
    assert record.saldo_contract == 5000.0
    assert record.status_contract == "NS"


@pytest.mark.django_db
def test_contract_put_nok_sup(commercial, gestionnaire, support_client):
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    contract = Contract(customer_id=customer.id,
                        sign_date="2023-12-21",
                        amount_contract=10000,
                        saldo_contract=5000,
                        status_contract="NS",
                        author_user=gestionnaire)
    contract.save()
    data = {
        "sign_date": "2023-11-30",
        "amount_contract": "50000",
        "saldo_contract": "4000",
        "status_contract": "NS",
    }
    response = support_client.put(f"/customers/{customer.id}/contracts/{contract.id}/", data=data)
    record = get_object_or_404(Contract, pk=contract.id)
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert record.sign_date == datetime.date(2023, 12, 21)
    assert record.amount_contract == 10000.0
    assert record.saldo_contract == 5000.0
    assert record.status_contract == "NS"
