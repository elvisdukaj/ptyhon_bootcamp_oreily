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


def get_user_info(user_id: int = 0) -> FullUserProfile:
    user_content = users_content[user_id]
    profile_info = profiles_info[user_id]

    user = User(**user_content)

    full_username = {
        **profile_info,
        **user.dict()
    }

    return FullUserProfile(**full_username)


def create_user(profile: FullUserProfile) -> int:
    global users_content
    global profiles_info

    new_user_id = len(users_content)
    username = profile.username
    liked_post = profile.liked_posts

    short_bio = profile.short_bio
    long_bio = profile.long_bio

    users_content[new_user_id] = {"liked_posts": liked_post}
    profiles_info[new_user_id] = {
        "short_bio": short_bio,
        "long_bio": long_bio
    }

    return new_user_id


@app.get("/", response_class=PlainTextResponse)
def home():
    return "new hello world"


@app.get("/user/me", response_model=FullUserProfile)
def user_info():
    return get_user_info()


@app.get("/usr/{user_id}", response_model=FullUserProfile)
def get_user_by_id(user_id: int):
    return get_user_info(user_id)


@app.post("/users", response_model=CreateUserResponse)
def add_user(full_profile_info: FullUserProfile):
    user_id = create_user(full_profile_info)
    response = CreateUserResponse(user_id=user_id)
    return response
