import pytest

from rest_framework import status
from events.models import Customer


@pytest.mark.django_db
def test_contract_amount_neg(commercial, gestionnaire_client):
    """Create contract nok, role COM"""
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    data = {
            "sign_date": "2023-10-31T15:17:00Z",
            "amount_contract": "-20000",
            "saldo_contract": "3000",
            "status_contract": "SI",
            }
    response = gestionnaire_client.post(f"/customers/{customer.id}/contracts/", data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.content
    assert str(response.data["non_field_errors"][0]) == 'this amount is negative'


@pytest.mark.django_db
def test_contract_saldo_neg(commercial, gestionnaire_client):
    """Create contract nok, role COM"""
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    data = {
            "sign_date": "2023-10-31T15:17:00Z",
            "amount_contract": "20000",
            "saldo_contract": "-3000",
            "status_contract": "SI"
    }
    response = gestionnaire_client.post(f"/customers/{customer.id}/contracts/", data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.content
    assert str(response.data["non_field_errors"][0]) == 'this amount is negative'


@pytest.mark.django_db
def test_contract_saldo_sup_amount(commercial, gestionnaire_client):
    """Create contract nok, role COM"""
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    data = {
            "sign_date": "2023-10-31T15:17:00Z",
            "amount_contract": "2000",
            "saldo_contract": "3000",
            "status_contract": "SI",
    }
    response = gestionnaire_client.post(f"/customers/{customer.id}/contracts/", data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.content
    assert str(response.data["non_field_errors"][0]) == 'Saldo is more than the amount'


@pytest.mark.django_db
def test_contract_bad_status(commercial, gestionnaire_client):
    """Create contract nok, role COM"""
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    data = {
            "sign_date": "2023-10-31T15:17:00Z",
            "amount_contract": "2000",
            "saldo_contract": "1000",
            "status_contract": "ad",
    }
    response = gestionnaire_client.post(f"/customers/{customer.id}/contracts/", data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.content
    assert str(response.data["status_contract"][0]) == '"ad" is not a valid choice.'
