from fastapi.testclient import TestClient
import pytest
from main import create_application


@pytest.fixture(scope="function")
def mocking_app():
    app = create_application()
    mock = TestClient(app)
    return mock
