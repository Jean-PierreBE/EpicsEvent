import pytest
from rest_framework import status
from users_api.models import UserProfile


@pytest.mark.django_db
def test_put_super_user(superuser_client):
    user_test = UserProfile(pseudo="test01",
                            first_name="prenom01",
                            last_name="nom01",
                            email="nom01@mail.be",
                            role="COM",
                            password="Ulysse1786")
    user_test.save()
    response = superuser_client.delete(f"/signup/{user_test.id}/")
    assert response.status_code == status.HTTP_204_NO_CONTENT, response.content


@pytest.mark.django_db
def test_put_ges_user(ges_client):
    user_test = UserProfile(pseudo="test01",
                            first_name="prenom01",
                            last_name="nom01",
                            email="nom01@mail.be",
                            role="COM",
                            password="Ulysse1786")
    user_test.save()
    response = ges_client.delete(f"/signup/{user_test.id}/")
    assert response.status_code == status.HTTP_204_NO_CONTENT, response.content


@pytest.mark.django_db
def test_put_com_user(com_client):
    user_test = UserProfile(pseudo="test01",
                            first_name="prenom01",
                            last_name="nom01",
                            email="nom01@mail.be",
                            role="COM",
                            password="Ulysse1786")
    user_test.save()
    response = com_client.delete(f"/signup/{user_test.id}/")
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content


@pytest.mark.django_db
def test_put_sup_user(sup_client):
    user_test = UserProfile(pseudo="test01",
                            first_name="prenom01",
                            last_name="nom01",
                            email="nom01@mail.be",
                            role="COM",
                            password="Ulysse1786")
    user_test.save()
    response = sup_client.delete(f"/signup/{user_test.id}/")
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
