from fastapi import (
    HTTPException,
    Response
)
import time


response_count: int = 0
response_start_time: float = time.time()
response_interval: float = 30.0  # seconds
response_limit_rate: int = 5  # maximum replies in the interval


def rate_limit(response: Response) -> Response:
    global response_start_time
    global response_count

    current_time = time.time()

    if current_time > response_start_time + response_interval:
        response_start_time = current_time
        response_count = 0

    if response_count >= response_limit_rate:
        raise HTTPException(
            status_code=429,
            detail={"error": "rate limit exceeded",
                    "timeout": round(response_start_time + response_interval - time.time(), 2) + 0.01
                    }
        )

    response_count += 1
    response.headers["X-app-rate-limit"] = f"{response_count}:{response_limit_rate}"

    return response
