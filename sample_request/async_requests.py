import asyncio
import aiohttp


async def sample_async_get_request():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:8080/user/0") as response:
            print(f"status code: {response.status}")
            print(f"header: {response.headers}")
            print(await response.json())

async def sample_async_post_request():
    async with aiohttp.ClientSession() as session:
        sample_data_to_send = {
            "name": "Alice Grimandi",
            "liked_posts": [1, 2, 3],
            "short_bio": "It was my ex",
            "long_bio": "she still is in love with me"
        }
        async with session.post("http://127.0.0.1:8080/user", json=sample_data_to_send) as response:
            print(f"status code: {response.status}")
            print(f"header: {response.headers}")
            print(await response.json())


asyncio.run(sample_async_get_request())
