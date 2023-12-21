import pytest
from rest_framework import status
from users_api.models import UserProfile
from users_api.constants import PASSWORD_TEST


@pytest.mark.django_db
def test_delete_super_user(superuser_client):
    user_test = UserProfile(pseudo="test01",
                            first_name="prenom01",
                            last_name="nom01",
                            email="nom01@mail.be",
                            role="COM",
                            password=PASSWORD_TEST)
    user_test.save()
    response = superuser_client.delete(f"/signup/{user_test.id}/")
    count = UserProfile.objects.filter(id=user_test.id).count()
    assert response.status_code == status.HTTP_204_NO_CONTENT, response.content
    assert count == 0


@pytest.mark.django_db
def test_delete_ges_user(ges_client):
    user_test = UserProfile(pseudo="test01",
                            first_name="prenom01",
                            last_name="nom01",
                            email="nom01@mail.be",
                            role="COM",
                            password=PASSWORD_TEST)
    user_test.save()
    response = ges_client.delete(f"/signup/{user_test.id}/")
    count = UserProfile.objects.filter(id=user_test.id).count()
    assert response.status_code == status.HTTP_204_NO_CONTENT, response.content
    assert count == 0


@pytest.mark.django_db
def test_delete_com_user(com_client):
    user_test = UserProfile(pseudo="test01",
                            first_name="prenom01",
                            last_name="nom01",
                            email="nom01@mail.be",
                            role="COM",
                            password=PASSWORD_TEST)
    user_test.save()
    response = com_client.delete(f"/signup/{user_test.id}/")
    count = UserProfile.objects.filter(id=user_test.id).count()
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert count == 1


@pytest.mark.django_db
def test_delete_sup_user(sup_client):
    user_test = UserProfile(pseudo="test01",
                            first_name="prenom01",
                            last_name="nom01",
                            email="nom01@mail.be",
                            role="SUP",
                            password=PASSWORD_TEST)
    user_test.save()
    response = sup_client.delete(f"/signup/{user_test.id}/")
    count = UserProfile.objects.filter(id=user_test.id).count()
    assert response.status_code == status.HTTP_403_FORBIDDEN, response.content
    assert count == 1
