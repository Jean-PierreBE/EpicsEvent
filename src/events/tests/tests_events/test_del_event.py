import pytest
from rest_framework import status
from events.models import Customer, Contract, Event


@pytest.mark.django_db
def test_event_delete_ok_ges(gestionnaire, support, commercial, gestionnaire_client):
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
    response = gestionnaire_client.delete(f"/customers/{customer.id}/contracts/{contract.id}/events/{event.id}/")
    assert response.status_code == status.HTTP_204_NO_CONTENT, response.content


@pytest.mark.django_db
def test_event_delete_ok_sup(gestionnaire, support, commercial, support_client):
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
    response = support_client.delete(f"/customers/{customer.id}/contracts/{contract.id}/events/{event.id}/")
    assert response.status_code == status.HTTP_204_NO_CONTENT, response.content


@pytest.mark.django_db
def test_event_delete_nok_sup(gestionnaire, support, commercial, support01_client):
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
    response = support01_client.delete(f"/customers/{customer.id}/contracts/{contract.id}/events/{event.id}/")
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content


@pytest.mark.django_db
def test_event_delete_nok_com(gestionnaire, support, commercial, commercial_client):
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
    response = commercial_client.delete(f"/customers/{customer.id}/contracts/{contract.id}/events/{event.id}/")
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
