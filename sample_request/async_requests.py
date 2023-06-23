import asyncio
import aiohttp


async def sample_async_get_request(base_url: str, endpoint_prefix: str, user_id: int):
    url = f"{base_url}/{endpoint_prefix}/{user_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            json_response = await response.json()
            status_code = response.status
            return status_code, json_response, response.headers


async def sample_async_post_request(base_url: str, endpoint_prefix: str, user_id: int):
    url = f"{base_url}/{endpoint_prefix}/{user_id}"
    async with aiohttp.ClientSession() as session:
        sample_data_to_send = {
            "name": "Olta Dukaj",
            "liked_posts": [1, 2, 3],
            "short_bio": "She's my sister",
            "long_bio": "She's with Marco and has Noah"
        }
        async with session.post(url, json=sample_data_to_send) as response:
            print(f"status code: {response.status}")
            print(f"header: {response.headers}")
            print(await response.json())


# asyncio.run(sample_async_get_request())
