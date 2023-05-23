from typing import Optional

from app.schemas.user import FullUserProfile, User
from app.exceptions import UserNotFoundError

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


class UserService:
    def __init__(self):
        pass

    async def get_all_users_paginated(self, start: int, count: int):
        list_of_users = []

        keys = list(users_content.keys())

        for index in range(0, len(keys)):
            if index < start:
                continue

            current_user_key = keys[index]
            user = await self.get_user_by_id(current_user_key)
            list_of_users.append(user)

            if len(list_of_users) >= count:
                break

        return list_of_users, len(keys)

    @staticmethod
    async def get_user_by_id(user_id: int = 0) -> FullUserProfile:
        if user_id not in users_content:
            raise UserNotFoundError(user_id)

        user_content = users_content[user_id]
        profile_info = profiles_info[user_id]

        user = User(**user_content)

        full_username = {
            **profile_info,
            **user.dict()
        }

        return FullUserProfile(**full_username)

    @staticmethod
    async def create_or_update_user(profile: FullUserProfile, new_user_id: Optional[int] = None) -> int:
        global users_content
        global profiles_info

        if new_user_id is None:
            new_user_id = len(users_content)

        username = profile.username
        liked_post = profile.liked_posts

        short_bio = profile.short_bio
        long_bio = profile.long_bio

        users_content[new_user_id] = {"username": username, "liked_posts": liked_post}
        profiles_info[new_user_id] = {
            "short_bio": short_bio,
            "long_bio": long_bio
        }

        return new_user_id

    @staticmethod
    async def delete_user(user_id: int) -> None:
        global users_content
        global profiles_info

        if user_id not in users_content:
            raise UserNotFoundError(user_id)

        del users_content[user_id]
        del profiles_info[user_id]
