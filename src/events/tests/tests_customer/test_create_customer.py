import pytest
from rest_framework import status
from django.shortcuts import get_object_or_404
from events.models import Customer


@pytest.mark.django_db
def test_customer_create_ok_com(commercial_client):
    data = {
        "enterprise_name": "BELGACOM",
        "client_name": "moi",
        "information": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum interdum",
        "email": "stein01@mail.be",
        "phone": "+32486303558"
    }
    response = commercial_client.post("/customers/", data=data)
    response_dict = response.json()
    record = get_object_or_404(Customer, pk=response_dict["id"])
    assert response.status_code == status.HTTP_201_CREATED, response.content
    assert record.enterprise_name == "BELGACOM"
    assert record.client_name == "moi"
    assert record.information == "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum interdum"
    assert record.email == "stein01@mail.be"
    assert record.phone == "+32486303558"


@pytest.mark.django_db
def test_customer_create_nok_ges(gestionnaire_client):
    data = {
        "enterprise_name": "BELGACOM",
        "client_name": "moi",
        "information": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum interdum ",
        "email": "stein01@mail.be",
        "phone": "+32486303558"
    }
    response = gestionnaire_client.post("/customers/", data=data)
    count = Customer.objects.filter(enterprise_name="BELGACOM").count()
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert count == 0


@pytest.mark.django_db
def test_customer_create_nok_sup(support_client):
    data = {
        "enterprise_name": "BELGACOM",
        "client_name": "moi",
        "information": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean interdum interdum ",
        "email": "stein01@mail.be",
        "phone": "+32486303558"
    }
    response = support_client.post("/customers/", data=data)
    count = Customer.objects.filter(enterprise_name="BELGACOM").count()
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert count == 0
