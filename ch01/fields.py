from fastapi import FastAPI
from typing import Optional

from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, Field

app = FastAPI()


class User(BaseModel):
    user_name: str = Field(
        alias="name",
        title="The username",
        default="None"
    )

    liked_posts: list[int] = Field(
        description="Array of liked posts",
        min_items=2,
        max_items=10
    )


class FullUserProfile(User):
    short_bio: str
    long_bio: str


def get_user_info() -> User:
    profile_bio = {
        "short_bio": "he is cool",
        "long_bio": "He is a very cool guy, this bio is most probably longer than 20 charachters"
    }

    user = {
        "name": "Elvis Dukaj",
        "liked_posts": [1, 2, 3]
    }

    user = User(**user)
    full_username = {
        **profile_bio,
        **user.dict()
    }

    return FullUserProfile(**full_username)


@app.get("/", response_class=PlainTextResponse)
def home():
    return "new hello world"


@app.get("/user/me", response_model=FullUserProfile)
def user_info():
    return get_user_info()
