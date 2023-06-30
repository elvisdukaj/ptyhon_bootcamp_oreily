import os

from fastapi import FastAPI
from app.routes.user import create_user_router
from app.exception_handlers import add_exception_handlers


def create_application():
    fast_app = FastAPI()

    users_content, profiles_info = create_users_content_and_profiles_info()
    user_route = create_user_router(users_content=users_content, profiles_info=profiles_info)

    fast_app.include_router(user_route)
    add_exception_handlers(fast_app)

    return fast_app


def create_users_content_and_profiles_info():
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

    return users_content, profiles_info




from models import recreate_postgres_tables

recreate_postgres_tables()

app = create_application()
