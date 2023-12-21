import pytest
from rest_framework import status
from events.models import Customer, Contract


@pytest.mark.django_db
def test_contract_list_all(commercial, gestionnaire, gestionnaire_client):
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
    contract = Contract(customer_id=customer.id,
                        sign_date="2023-12-24",
                        amount_contract=10000,
                        saldo_contract=5000,
                        status_contract="SI",
                        author_user=gestionnaire)
    contract.save()
    response = gestionnaire_client.get(f"/customers/{customer.id}/contracts/")
    count = Contract.objects.filter(customer_id=customer.id).count()
    assert response.status_code == status.HTTP_200_OK, response.content
    assert count == 2


@pytest.mark.django_db
def test_contract_list_one(commercial, gestionnaire, gestionnaire_client):
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
    response = gestionnaire_client.get(f"/customers/{customer.id}/contracts/{contract.id}/")
    count = Contract.objects.filter(id=contract.id).count()
    assert response.status_code == status.HTTP_200_OK, response.content
    assert count == 1
