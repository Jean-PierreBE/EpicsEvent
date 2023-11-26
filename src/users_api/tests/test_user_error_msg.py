import pytest
from rest_framework import status


@pytest.mark.django_db
def test_role_error(ges_client):
    data = {
        "pseudo": "test02",
        "first_name": "prenom01",
        "last_name": "nom01",
        "email": "test02@mail.be",
        "role": "ad",
        "password": "Ulysse1786",
    }
    response = ges_client.post("/signup/", data=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.content
    assert str(response.data["role"][0]) == '"ad" is not a valid choice.'
