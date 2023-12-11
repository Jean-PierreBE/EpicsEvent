import pytest
from rest_framework import status
from events.models import Customer, Contract, Event


@pytest.mark.django_db
def test_event_put_ok_ges(gestionnaire, support, commercial, gestionnaire_client):
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
    event = Event(begin_date="2023-10-31",
                  begin_hour="12:00:00",
                  end_date="2023-10-31",
                  end_hour="18:00:00",
                  location="ici",
                  notes="ras",
                  attendees_count=10,
                  support_user_id=support.id,
                  contract_id=contract.id,
                  author_user=commercial)
    event.save()
    data = {
        "begin_date": "2023-12-31",
        "begin_hour": "12:00:00",
        "end_date": "2023-12-31",
        "end_hour": "23:00:00",
        "location": "ailleurs",
        "notes": "ras",
        "attendees_count": 100,
        "contract_id": contract.id,
        "support_user": support.id
    }
    response = gestionnaire_client.put(f"/customers/{customer.id}/contracts/{contract.id}/events/{event.id}/",
                                       data=data)
    assert response.status_code == status.HTTP_200_OK, response.content


@pytest.mark.django_db
def test_event_put_ok_sup(gestionnaire, support, commercial, support_client):
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
    event = Event(begin_date="2023-10-31",
                  begin_hour="12:00:00",
                  end_date="2023-10-31",
                  end_hour="18:00:00",
                  location="ici",
                  notes="ras",
                  attendees_count=10,
                  support_user_id=support.id,
                  contract_id=contract.id,
                  author_user=commercial)
    event.save()
    data = {
        "begin_date": "2023-12-31",
        "begin_hour": "12:00:00",
        "end_date": "2023-12-31",
        "end_hour": "23:00:00",
        "location": "ailleurs",
        "notes": "ras",
        "attendees_count": 100,
        "contract_id": contract.id,
        "support_user": support.id
    }
    response = support_client.put(f"/customers/{customer.id}/contracts/{contract.id}/events/{event.id}/", data=data)
    assert response.status_code == status.HTTP_200_OK, response.content


@pytest.mark.django_db
def test_event_put_nok_sup(gestionnaire, support, commercial, support01_client):
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
    event = Event(begin_date="2023-10-31",
                  begin_hour="12:00:00",
                  end_date="2023-10-31",
                  end_hour="18:00:00",
                  location="ici",
                  notes="ras",
                  attendees_count=10,
                  support_user_id=support.id,
                  contract_id=contract.id,
                  author_user=commercial)
    event.save()
    data = {
        "begin_date": "2023-12-31",
        "begin_hour": "12:00:00",
        "end_date": "2023-12-31",
        "end_hour": "23:00:00",
        "location": "ailleurs",
        "notes": "ras",
        "attendees_count": 100,
        "contract_id": contract.id,
        "support_user": support.id
    }
    response = support01_client.put(f"/customers/{customer.id}/contracts/{contract.id}/events/{event.id}/", data=data)
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
