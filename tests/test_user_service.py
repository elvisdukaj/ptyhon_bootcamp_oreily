import pytest
from app.services.user import   UserService


@pytest.mark.asyncio
async def test_user_delete_works_properly():
    profiles_info: dict[int, dict] = {
        0: {
            "short_bio": "default",
            "long_bio": "default"
        },
        1: {
            "short_bio": "he is cool",
            "long_bio": "He is a very cool guy"
        }
    }

    users_content: dict[int, dict] = {
        0: {
            "username": "default",
            "liked_posts": []
        },
        1: {
            "username": "edukaj",
            "liked_posts": [1, 2, 3]
        }
    }

    user_service = UserService(users_content=users_content, profiles_info=profiles_info)
    user_to_delete = 0
    await user_service.delete_user(user_to_delete)
    assert user_to_delete not in users_content
    assert user_to_delete not in profiles_info
