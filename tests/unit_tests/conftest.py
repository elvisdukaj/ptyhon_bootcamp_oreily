_deimport pytest
from app.services.user import UserService


@pytest.fixture
def _profiles_info():
    val: dict[int, dict] = {
        0: {
            "short_bio": "default",
            "long_bio": "default"
        },
        1: {
            "short_bio": "he is cool",
            "long_bio": "He is a very cool guy"
        }
    }
    return val


@pytest.fixture
def _users_content():
    val: dict[int, dict] = {
        0: {
            "username": "default",
            "liked_posts": []
        },
        1: {
            "username": "edukaj",
            "liked_posts": [1, 2, 3]
        }
    }
    return val


@pytest.fixture
def user_service(_users_content, _profiles_info):
    user_service = UserService(_users_content, _profiles_info)
    return user_service
