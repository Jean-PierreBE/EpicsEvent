import pytest

from rest_framework import status
from events.models import Customer, Contract


# Version simple
@pytest.mark.django_db
def test_event_create_ok_ges(commercial, gestionnaire, commercial_client):
    """Create contract ok, role GES"""
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    print('commercial.id ' + str(commercial.id))

    customer.save()
    print('customer.id ' + str(customer.id))
    contract = Contract(sign_date="2023-10-31T15:17:00Z",
                        amount_contract="20000",
                        saldo_contract="3000",
                        status_contract="SI",
                        customer_id=customer.id,
                        author_user=gestionnaire)
    contract.save()
    print('contract.id ' + str(contract.id))
    data = {
        "client_name": "stein",
        "email": "stein@mail.be",
        "phone": "+32486303558",
        "begin_date": "2023-10-31T15:17:00Z",
        "end_date": "2023-10-31T15:17:00Z",
        "location": "ici",
        "notes": "ras",
        "attendees_count": 10,
        "support_user": gestionnaire.id
    }
    response = commercial_client.post(f"/customers/{customer.id}/contracts/{contract.id}/", data=data)
    assert response.status_code == status.HTTP_201_CREATED, response.content
