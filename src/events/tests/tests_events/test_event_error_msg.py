import pytest

from rest_framework import status
from events.models import Customer, Contract


@pytest.mark.django_db
def test_event_attendee_negative(gestionnaire, support, commercial, commercial_client):
    """Create contract ok, role GES"""
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    contract = Contract(sign_date="2023-10-31",
                        amount_contract="20000",
                        saldo_contract="3000",
                        status_contract="SI",
                        customer_id=customer.id,
                        author_user=gestionnaire)
    contract.save()
    data = {
        "begin_date": "2023-10-31",
        "begin_hour": "12:00:00",
        "end_date": "2023-10-31",
        "end_hour": "18:00:00",
        "location": "ici",
        "notes": "ras",
        "attendees_count": -10,
        "contract_id": contract.id,
        "support_user": support.id
    }
    response = commercial_client.post(f"/customers/{customer.id}/contracts/{contract.id}/events/", data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.content
    assert str(response.data["non_field_errors"][0]) == 'attendees is negative'


@pytest.mark.django_db
def test_event_not_sup(gestionnaire, commercial, commercial_client):
    """Create contract ok, role GES"""
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    contract = Contract(sign_date="2023-10-31",
                        amount_contract="20000",
                        saldo_contract="3000",
                        status_contract="SI",
                        customer_id=customer.id,
                        author_user=gestionnaire)
    contract.save()
    data = {
        "begin_date": "2023-10-31",
        "begin_hour": "12:00:00",
        "end_date": "2023-10-31",
        "end_hour": "18:00:00",
        "location": "ici",
        "notes": "ras",
        "attendees_count": -10,
        "contract_id": contract.id,
        "support_user": gestionnaire.id
    }
    response = commercial_client.post(f"/customers/{customer.id}/contracts/{contract.id}/events/", data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.content
    assert str(response.data["non_field_errors"][0]) == 'this user is not SUP'
