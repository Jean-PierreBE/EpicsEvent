import pytest
from rest_framework import status
from events.models import Customer


@pytest.mark.django_db
def test_list_one_customer(commercial, commercial_client):
    customer = Customer(enterprise_name='BELGACOM',
                        client_name='moi',
                        information='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ',
                        email='stein@mail.be',
                        phone='+32486303558',
                        author_user=commercial)
    customer.save()
    response = commercial_client.get(f"/customers/{customer.id}/")
    count = Customer.objects.filter(id=customer.id).count()
    assert response.status_code == status.HTTP_200_OK, response.content
    assert count == 1


@pytest.mark.django_db
def test_list_all_customer(commercial, commercial_client):
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
    count = Customer.objects.filter(author_user_id=commercial.id).count()
    assert response.status_code == status.HTTP_200_OK, response.content
    assert count == 2
