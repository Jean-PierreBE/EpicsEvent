import pytest
from rest_framework import status
from events.models import Customer


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
    assert response.status_code == status.HTTP_204_NO_CONTENT, response.content


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
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content


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
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
