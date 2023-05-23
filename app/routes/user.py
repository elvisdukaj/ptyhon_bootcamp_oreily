from fastapi import (
    APIRouter,
    Depends
)
from app.schemas.user import (
    CreateUserResponse,
    FullUserProfile,
    UserListResponse
)
from app.services.user import UserService
import logging
from app.dependencies import rate_limit

logger = logging.getLogger(__name__)


def create_user_router(users_content: dict, profiles_info: dict):
    user_route = APIRouter(
        prefix="/user",
        tags=["user"],
        dependencies=[Depends(rate_limit)]
    )
    user_service = UserService(users_content=users_content, profiles_info=profiles_info)

    @user_route.post("/", response_model=CreateUserResponse, status_code=201)
    async def add_user_endpoint(full_profile_info: FullUserProfile):
        user_id = await user_service.create_or_update_user(full_profile_info)
        response = CreateUserResponse(user_id=user_id)
        return response

    @user_route.get("/all", response_model=UserListResponse)
    async def get_all_users_paginated_endpoint(start: int = 0, count: int = 2):
        users, total_users = await user_service.get_all_users_paginated(start, count)
        response = UserListResponse(users=users, total_users=total_users)
        return response

    @user_route.get("/{user_id}", response_model=FullUserProfile)
    async def get_user_by_id_endpoint(user_id: int):
        full_user_profile = await user_service.get_user_by_id(user_id)
        return full_user_profile

    @user_route.put("/{user_id}")
    async def update_or_create_user_endpoint(user_id: int, full_user_profile: FullUserProfile):
        await user_service.create_or_update_user(profile=full_user_profile, new_user_id=user_id)

    @user_route.delete("/{user_id}")
    async def delete_user_endpoint(user_id: int):
        await user_service.delete_user(user_id)

    return user_route
