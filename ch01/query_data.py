from fastapi import FastAPI
from typing import Optional

from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, Field

app = FastAPI()

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


class User(BaseModel):
    username: str = Field(
        title="The username",
        description="This is the username of the user",
        default=None
    )

    liked_posts: list[int] = Field(
        description="Array of liked posts",
    )


class FullUserProfile(User):
    short_bio: str
    long_bio: str


class CreateUserResponse(BaseModel):
    user_id: int


class UserListResponse(BaseModel):
    users: list[FullUserProfile]
    total_users: int


def get_user_by_id(user_id: int = 0) -> FullUserProfile:
    user_content = users_content[user_id]
    profile_info = profiles_info[user_id]

    user = User(**user_content)

    full_username = {
        **profile_info,
        **user.dict()
    }

    return FullUserProfile(**full_username)


def create_or_update_user(profile: FullUserProfile, new_user_id: Optional[int] = None) -> int:
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


def delete_user(user_id: int) -> None:
    global users_content
    global profiles_info

    del users_content[user_id]
    del profiles_info[user_id]


def get_all_users_paginated(start: int, count: int):
    list_of_users = []

    keys = list(users_content.keys())

    for index in range(0, len(keys)):
        if index < start:
            continue

        current_user_key = keys[index]
        user = get_user_by_id(current_user_key)
        list_of_users.append(user)

        if len(list_of_users) >= count:
            break

    return list_of_users, len(keys)


@app.get("/", response_class=PlainTextResponse)
def home():
    return "new hello world"


@app.get("/user/me", response_model=FullUserProfile)
def user_info_endpoint():
    return get_user_by_id()


@app.get("/usr/{user_id}", response_model=FullUserProfile)
def get_user_by_id_endpoint(user_id: int):
    return get_user_by_id(user_id)


@app.get("/users", response_model=UserListResponse)
def get_all_users_paginated_endpoint(start: int = 0, count: int = 2):
    users, total_users = get_all_users_paginated(start, count)
    response = UserListResponse(users=users, total_users=total_users)
    return response


@app.post("/users", response_model=CreateUserResponse)
def add_user_endpoint(full_profile_info: FullUserProfile):
    user_id = create_or_update_user(full_profile_info)
    response = CreateUserResponse(user_id=user_id)
    return response


@app.put("/users/{user_id}")
def update_or_create_user_endpoint(user_id: int, full_user_profile: FullUserProfile):
    create_or_update_user(profile=full_user_profile, new_user_id=user_id)


@app.delete("/users/{user_id}")
def delete_user_endpoint(user_id: int):
    delete_user(user_id)
