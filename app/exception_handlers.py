import fastapi
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.exceptions import UserNotFoundError
import logging

logger = logging.getLogger(__name__)


def add_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(UserNotFoundError)
    async def handler_user_not_found_exception(request: fastapi.Request, exc: UserNotFoundError):
        logger.error(f"User id {exc.user_id} was not found")
        return JSONResponse(status_code=404, content=f"user id user_id not found")

    return None
