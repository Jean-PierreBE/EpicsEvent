import pytest
from rest_framework import status
import datetime
from django.shortcuts import get_object_or_404
from events.models import Customer, Contract, Event


@pytest.mark.django_db
def test_event_create_ok_com(gestionnaire, support, commercial, commercial_client):
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
        "attendees_count": 10,
        "contract_id": contract.id,
        "support_user": support.id
    }
    response = commercial_client.post(f"/customers/{customer.id}/contracts/{contract.id}/events/", data=data)
    response_dict = response.json()
    record = get_object_or_404(Event, pk=response_dict["id"])
    assert response.status_code == status.HTTP_201_CREATED, response.content
    assert record.begin_date == datetime.date(2023, 10, 31)
    assert record.begin_hour == datetime.time(12, 0, 0)
    assert record.end_date == datetime.date(2023, 10, 31)
    assert record.end_hour == datetime.time(18, 0, 0)
    assert record.location == "ici"
    assert record.notes == "ras"
    assert record.attendees_count == 10


@pytest.mark.django_db
def test_event_create_nok_com(gestionnaire, support, commercial, commercial01_client):
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
        "attendees_count": 10,
        "contract_id": contract.id,
        "support_user": support.id
    }
    response = commercial01_client.post(f"/customers/{customer.id}/contracts/{contract.id}/events/", data=data)
    count = Event.objects.filter(contract_id=contract.id).count()
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert count == 0


@pytest.mark.django_db
def test_event_create_nok_sup(gestionnaire, support, commercial, support01_client):
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
        "attendees_count": 10,
        "contract_id": contract.id,
        "support_user": support.id
    }
    response = support01_client.post(f"/customers/{customer.id}/contracts/{contract.id}/events/", data=data)
    count = Event.objects.filter(contract_id=contract.id).count()
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert count == 0


@pytest.mark.django_db
def test_event_create_nok_ges(gestionnaire, support, commercial, gestionnaire_client):
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
        "attendees_count": 10,
        "contract_id": contract.id,
        "support_user": support.id
    }
    response = gestionnaire_client.post(f"/customers/{customer.id}/contracts/{contract.id}/events/", data=data)
    count = Event.objects.filter(contract_id=contract.id).count()
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert count == 0
