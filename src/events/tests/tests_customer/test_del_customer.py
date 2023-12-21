import pytest
from rest_framework import status
from events.models import Customer, Contract, Event


# Version simple
@pytest.mark.django_db
def test_contract_del_ok_com(commercial, commercial_client):
    """Create contract ok, role GES"""
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    response = commercial_client.delete(f"/customers/{customer.id}/")
    count = Customer.objects.filter(id=customer.id).count()
    assert response.status_code == status.HTTP_204_NO_CONTENT, response.content
    assert count == 0


@pytest.mark.django_db
def test_contract_del_nok_ges(commercial, gestionnaire_client):
    """Create contract nok, role COM"""
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    response = gestionnaire_client.delete(f"/customers/{customer.id}/")
    count = Customer.objects.filter(id=customer.id).count()
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert count == 1


@pytest.mark.django_db
def test_contract_del_nok_sup(commercial, support_client):
    """Create contract nok, role COM"""
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    response = support_client.delete(f"/customers/{customer.id}/")
    count = Customer.objects.filter(id=customer.id).count()
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert count == 1


@pytest.mark.django_db
def test_customer_delete_cascade(gestionnaire, support, commercial, commercial_client):
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
    response = commercial_client.delete(f"/customers/{customer.id}/")
    count_event = Event.objects.filter(id=event.id).count()
    count_contract = Contract.objects.filter(id=contract.id).count()
    count_customer = Customer.objects.filter(id=customer.id).count()
    assert response.status_code == status.HTTP_204_NO_CONTENT, response.content
    assert count_event == 0
    assert count_contract == 0
    assert count_customer == 0
