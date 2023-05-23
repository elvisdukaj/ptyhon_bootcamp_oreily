import pytest


@pytest.mark.asyncio
async def test_user_delete_works_properly(user_service):
    user_to_delete = 0
    await user_service.delete_user(user_to_delete)
    assert user_to_delete not in user_service.users_content
    assert user_to_delete not in user_service.profiles_info
