from fastapi import FastAPI
from app.routes.user import create_user_router
from app.exception_handlers import add_exception_handlers


def create_application():
    fast_app = FastAPI()

    user_route = create_user_router()

    fast_app.include_router(user_route)
    add_exception_handlers(fast_app)

    return fast_app


app = create_application()
