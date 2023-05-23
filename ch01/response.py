from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class ProfileBio(BaseModel):
    short_bio: str
    long_bio: str


class User(BaseModel):
    user_name: str
    profile_bio: ProfileBio
    liked_posts: Optional[list[int]]


def get_user_info() -> User:
    profile_bio = {
        "short_bio": "he is cool",
        "long_bio": "He is a very cool guy"
    }

    user = {
        "user_name": "Elvis Dukaj",
        "profile_bio": profile_bio,
        "liked_posts": [1, 2, 3]
    }

    return User(**user)


@app.get("/", response_class=PlainTextResponse)
def home():
    return "new hello world"


@app.get("/user/me", response_model=User)
def user_info():
    return get_user_info()
