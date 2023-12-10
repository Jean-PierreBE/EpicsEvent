import pytest
from rest_framework import status
from events.models import Customer


@pytest.mark.django_db
def test_signup_one_customer(commercial, commercial_client):
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    response = commercial_client.get(f"/customers/{customer.id}/")
    assert response.status_code == status.HTTP_200_OK, response.content

@pytest.mark.django_db
def test_signup_all_customer(commercial, commercial_client):
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='steinMANN@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    customer = Customer(enterprise_name='PROXIMUS',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    response = commercial_client.get("/customers/")
    assert response.status_code == status.HTTP_200_OK, response.content