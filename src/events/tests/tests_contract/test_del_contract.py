import pytest
from rest_framework import status
from events.models import Customer, Contract, Event


@pytest.mark.django_db
def test_contract_delete_ok_ges(commercial, gestionnaire, gestionnaire_client):
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
    response = gestionnaire_client.delete(f"/customers/{customer.id}/contracts/{contract.id}/")
    count = Contract.objects.filter(id=contract.id).count()
    assert response.status_code == status.HTTP_204_NO_CONTENT, response.content
    assert count == 0


@pytest.mark.django_db
def test_contract_delete_ok_same_com(commercial, gestionnaire, commercial_client):
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
    response = commercial_client.delete(f"/customers/{customer.id}/contracts/{contract.id}/")
    count = Contract.objects.filter(id=contract.id).count()
    assert response.status_code == status.HTTP_204_NO_CONTENT, response.content
    assert count == 0


@pytest.mark.django_db
def test_contract_delete_nok_diff_com(commercial, gestionnaire, commercial01_client):
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
    response = commercial01_client.delete(f"/customers/{customer.id}/contracts/{contract.id}/")
    count = Contract.objects.filter(id=contract.id).count()
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert count == 1


@pytest.mark.django_db
def test_contract_delete_nok_sup(commercial, gestionnaire, support_client):
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
    response = support_client.delete(f"/customers/{customer.id}/contracts/{contract.id}/")
    count = Contract.objects.filter(id=contract.id).count()
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert count == 1


@pytest.mark.django_db
def test_contract_delete_cascade(gestionnaire, support, commercial, commercial_client):
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
    response = commercial_client.delete(f"/customers/{customer.id}/contracts/{contract.id}/")
    count_event = Event.objects.filter(id=event.id).count()
    count_contract = Contract.objects.filter(id=contract.id).count()
    count_customer = Customer.objects.filter(id=customer.id).count()
    assert response.status_code == status.HTTP_204_NO_CONTENT, response.content
    assert count_event == 0
    assert count_contract == 0
    assert count_customer == 1
