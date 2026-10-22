import uuid

import pytest

from api_practice.api_client.api_client import ApiClient


@pytest.fixture
def api_client() -> ApiClient:
    return ApiClient()


@pytest.fixture
def pump_id() -> str:
    return f"test-pump-{uuid.uuid4()}"
