import pytest
from app.schemas.user import User, FullUserProfile


@pytest.fixture(scope="session")
def valid_user_id() -> int:
    return 0


@pytest.fixture(scope="session")
def invalid_user_delete_id() -> int:
    return 1000


@pytest.fixture(scope="session")
def sample_full_user_profile() -> FullUserProfile:
    return FullUserProfile(short_bio="the best", long_bio="the most wonderful", username="stefanie.zoechmann",
                           liked_posts=[1, 2])
