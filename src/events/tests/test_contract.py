from django.urls import reverse
import pytest

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from events.models import Customer


# Version simple
@pytest.mark.django_db
def test_contract_create(commercial, commercial_client):
    customer = Customer(enterprise_name= 'BELGACOM',
                        client_name= 'moi',
                        information= 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email= 'stein@mail.be',
                        phone= '+32486303558',
                        author_user = commercial)
    customer.save()
    data = {
            "sign_date":"2023-10-31T15:17:00Z",
            "amount_contract":"20000",
            "saldo_contract":"3000",
            "status_contract":"SI",
             }
    response = commercial_client.post(f"/customers/{customer.id}/contracts/", data=data)
    assert response.status_code == status.HTTP_201_CREATED, response.content
