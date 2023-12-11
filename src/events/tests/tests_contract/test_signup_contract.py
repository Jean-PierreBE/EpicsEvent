import pytest
from rest_framework import status
from events.models import Customer, Contract


@pytest.mark.django_db
def test_contract_signup_all(commercial, gestionnaire, gestionnaire_client):
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
    assert response.status_code == status.HTTP_200_OK, response.content


@pytest.mark.django_db
def test_contract_signup_one(commercial, gestionnaire, gestionnaire_client):
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
    assert response.status_code == status.HTTP_200_OK, response.content
