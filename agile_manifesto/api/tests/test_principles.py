import pytest
from django.urls import reverse
from rest_framework import status
from api.models import Principle
from django.core.management import call_command


def test_get_principle_list(api_client, load_principles):
    """
    loads data on db using load_principles fixture
    and checks if api_client can get the list successfully
    """
    path = reverse("principle-list")
    response = api_client.get(path)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 12


def test_add_principle(api_client, db):
    """
    counts initial number of records then posts one sample entry.
    rechecks if an entry was successfully created
    """
    assert Principle.objects.count() == 0
    data = {"title": "Principle #13", "text": "Sample Text"}
    path = reverse("principle-list")
    response = api_client.post(path, data=data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Principle.objects.count() == 1


@pytest.mark.parametrize("id", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
def test_get_principle_details(id, api_client, load_principles):
    """
    iterates function with incrementing id to check if
    records with pk from 1 to 4 can be fetched successfully
    """
    path = reverse("principle-detail", kwargs={"pk": id})
    response = api_client.get(path)
    assert response.data["title"] == "Principle #" + str(id)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_update_principle(api_client):
    """
    checks if update is successful
    """
    principle = Principle(title="Principle #1", text="Description #1")
    principle.save()
    path = reverse("principle-detail", kwargs={"pk": principle.pk})
    response = api_client.get(path)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    data["title"] = "New title"
    data["text"] = "New text"
    response = api_client.put(path, data=data, format="json")
    assert response.status_code == status.HTTP_200_OK
    principle.refresh_from_db()
    assert principle.title == data["title"]
    assert principle.text == data["text"]


@pytest.mark.django_db
@pytest.mark.parametrize("id", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
def test_delete_principle(id: int, api_client, load_principles):
    """
    iterates function and checks if item was successfully deleted
    """
    path = reverse("principle-detail", kwargs={"pk": id})
    assert Principle.objects.count() == 12
    response = api_client.delete(path)
    assert Principle.objects.count() == 11
    assert response.status_code == status.HTTP_204_NO_CONTENT
    response = api_client.get(path)
    assert response.status_code == status.HTTP_404_NOT_FOUND
