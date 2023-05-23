from fastapi import FastAPI
from typing import Optional

from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, Field

app = FastAPI()


class User(BaseModel):
    username: str = Field(
        alias="name",
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


def get_user_info(user_id="default") -> FullUserProfile:
    profiles_info = {
        "default": {
            "short_bio": "default",
            "long_bio": "default"
        },
        "edukaj": {
            "short_bio": "he is cool",
            "long_bio": "He is a very cool guy"
        }
    }

    profile_info = profiles_info[user_id]

    users_content = {
        "default": {
            "name": "default",
            "liked_posts": []
        },
        "edukaj": {
            "name": "edukaj",
            "liked_posts": [1, 2, 3]
        }
    }

    user_content = users_content[user_id]
    user = User(**user_content)

    full_username = {
        **profile_info,
        **user.dict()
    }

    return FullUserProfile(**full_username)


@app.get("/", response_class=PlainTextResponse)
def home():
    return "new hello world"


@app.get("/user/me", response_model=FullUserProfile)
def user_info():
    return get_user_info()


@app.get("/usr/{user_id}", response_model=FullUserProfile)
def get_user_by_id(user_id: str):
    return get_user_info(user_id)
