from sample_request.sync_requests import get_and_parse_user
import responses


@responses.activate
def test_get_and_parse_user_works_properly():
    base_url = 'http://someurl.com'
    endpoint_prefix = "user"
    user_id = 0

    res = responses.add(
        method=responses.GET,
        url=f"{base_url}/{endpoint_prefix}/{user_id}",
        json={"user": user_id},
        status=200,
        headers={}
    )

    response = get_and_parse_user(base_url=base_url, endpoint_prefix=endpoint_prefix, user_id=user_id)

    assert type(response) is dict
    assert response["user"] == user_id
