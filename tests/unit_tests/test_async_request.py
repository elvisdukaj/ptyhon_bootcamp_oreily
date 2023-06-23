from sample_request.async_requests import sample_async_get_request
from aioresponses import aioresponses
import pytest


@pytest.mark.asyncio
async def test_sample_async_get_request_works_properly():
    base_url = 'http://someurl.com'
    endpoint_prefix = "user"
    user_id = 0

    with aioresponses() as responses:
        responses.get(
            url=f"{base_url}/{endpoint_prefix}/{user_id}",
            payload={"user": user_id},
            status=200,
            headers={"some-header": "1"}
        )

        status_code, json_response, headers = await sample_async_get_request(base_url=base_url, endpoint_prefix=endpoint_prefix,
                                                                    user_id=user_id)

        assert status_code == 200
        assert json_response["user"] == user_id
        assert headers["some-header"] == "1"
