import pytest
from rest_framework import status
from users_api.models import UserProfile
from django.db.models import Q
from users_api.constants import PASSWORD_TEST


@pytest.mark.django_db
def test_list_one_user(superuser_client):
    user_test = UserProfile(pseudo="test01",
                            first_name="prenom01",
                            last_name="nom01",
                            email="nom01@mail.be",
                            role="COM",
                            password=PASSWORD_TEST)
    user_test.save()
    response = superuser_client.get(f"/signup/{user_test.id}/")
    count = UserProfile.objects.filter(id=user_test.id).count()
    assert response.status_code == status.HTTP_200_OK, response.content
    assert count == 1


@pytest.mark.django_db
def test_list_all_user(ges_user, ges_client):
    user_test = UserProfile(pseudo="test01",
                            first_name="prenom01",
                            last_name="nom01",
                            email="nom01@mail.be",
                            role="COM",
                            password=PASSWORD_TEST)
    user_test.save()
    user_test = UserProfile(pseudo="test02",
                            first_name="prenom02",
                            last_name="nom02",
                            email="nom02@mail.be",
                            role="GES",
                            password=PASSWORD_TEST)
    user_test.save()
    user_test = UserProfile(pseudo="test03",
                            first_name="prenom03",
                            last_name="nom03",
                            email="nom03@mail.be",
                            role="SUP",
                            password=PASSWORD_TEST)
    user_test.save()
    response = ges_client.get("/signup/")
    count = UserProfile.objects.filter(~Q(id=ges_user.id)).count()
    assert response.status_code == status.HTTP_200_OK, response.content
    assert count == 3
