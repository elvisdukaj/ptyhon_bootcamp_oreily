import requests


def get_and_parse_user(base_url: str, endpoint_prefix: str, user_id: int):
    url = f"{base_url}/{endpoint_prefix}/{user_id}"
    response = requests.get(url)
    return response.json()
