import pytest
from app.exceptions import UserNotFoundError


@pytest.mark.asyncio
async def test_user_delete_works_properly(user_service, valid_user_id):
    await user_service.delete_user(valid_user_id)
    assert valid_user_id not in user_service.users_content
    assert valid_user_id not in user_service.profiles_info


@pytest.mark.asyncio
async def test_delete_invalid_user_raises_proper_exception(user_service, invalid_user_delete_id):
    with pytest.raises(UserNotFoundError):
        await user_service.delete_user(invalid_user_delete_id)
        # don't put code here the above line is raising an exception
