from typing import Optional, Tuple

from app.schemas.user import FullUserProfile, User
from app.exceptions import UserNotFoundError


class UserService:
    def __init__(self, users_content: dict, profiles_info: dict):
        self.users_content = users_content
        self.profiles_info = profiles_info

    async def get_all_users_paginated(self, start: int, count: int) -> Tuple[list[FullUserProfile], int]:
        list_of_users = []

        keys = list(self.users_content.keys())

        for index in range(0, len(keys)):
            if index < start:
                continue

            current_user_key = keys[index]
            user = await self.get_user_by_id(current_user_key)
            list_of_users.append(user)

            if len(list_of_users) >= count:
                break

        return list_of_users, len(keys)

    async def get_user_by_id(self, user_id: int = 0) -> FullUserProfile:
        if user_id not in self.users_content:
            raise UserNotFoundError(user_id)

        user_content = self.users_content[user_id]
        profile_info = self.profiles_info[user_id]

        user = User(**user_content)

        full_username = {
            **profile_info,
            **user.dict()
        }

        return FullUserProfile(**full_username)

    async def create_or_update_user(self, profile: FullUserProfile, new_user_id: Optional[int] = None) -> int:
        if new_user_id is None:
            new_user_id = len(self.users_content)

        username = profile.username
        liked_post = profile.liked_posts

        short_bio = profile.short_bio
        long_bio = profile.long_bio

        self.users_content[new_user_id] = {"username": username, "liked_posts": liked_post}
        self.profiles_info[new_user_id] = {
            "short_bio": short_bio,
            "long_bio": long_bio
        }

        return new_user_id

    async def delete_user(self, user_id: int) -> None:
        if user_id not in self.users_content:
            raise UserNotFoundError(user_id)

        del self.users_content[user_id]
        del self.profiles_info[user_id]
