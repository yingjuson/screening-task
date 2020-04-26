import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.core.management import call_command
from api.models import Value


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture()
def load_values(db) -> None:
    call_command("loaddata", "values.json")


@pytest.fixture()
def load_principles(db) -> None:
    call_command("loaddata", "principles.json")
