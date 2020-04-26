import pytest
from django.urls import reverse
from rest_framework import status
from api.models import Value


def test_get_value_list(api_client, load_values):
    """
    loads data on db using load_values fixture
    and checks if api_client can get the list successfully
    """
    path = reverse("value-list")
    response = api_client.get(path)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 4


def test_add_value(api_client, load_values):
    """
    counts initial number of records then posts one sample entry.
    rechecks if an entry was successfully created
    """
    assert Value.objects.count() == 4
    data = {"title": "Value #1", "text": "Sample Text"}
    path = reverse("value-list")
    response = api_client.post(path, data=data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Value.objects.count() == 5


@pytest.mark.parametrize("id", [1, 2, 3, 4])
def test_get_value_details(id: int, api_client, load_values):
    """
    iterates function with incrementing id to check if
    records with pk value from 1 to 4 can be fetched successfully
    """
    path = reverse("value-detail", kwargs={"pk": id})
    response = api_client.get(path)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_update_value(api_client):
    """
    checks if update is successful
    """
    value_one = Value(title="Value #1", text="Description #1")
    value_one.save()
    path = reverse("value-detail", kwargs={"pk": value_one.pk})
    response = api_client.get(path)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    data["title"] = "New title"
    data["text"] = "New text"
    response = api_client.put(path, data=data, format="json")
    assert response.status_code == status.HTTP_200_OK
    value_one.refresh_from_db()
    assert value_one.title == data["title"]
    assert value_one.text == data["text"]


@pytest.mark.parametrize("id", [1, 2, 3, 4])
def test_delete_value(id: int, api_client, load_values):
    """
    iterates function and checks if item was successfully deleted
    """
    path = reverse("value-detail", kwargs={"pk": id})
    assert Value.objects.count() == 4
    response = api_client.delete(path)
    assert Value.objects.count() == 3
    assert response.status_code == status.HTTP_204_NO_CONTENT
    response = api_client.get(path)
    assert response.status_code == status.HTTP_404_NOT_FOUND
