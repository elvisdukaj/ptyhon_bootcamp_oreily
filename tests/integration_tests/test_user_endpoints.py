def test_user_delete_success(mocking_app, valid_user_id):
    response = mocking_app.delete(f"/user/{valid_user_id}")
    assert response.status_code == 200


def test_user_delete_failure(mocking_app, valid_user_id):
    response = mocking_app.delete(f"/user/{valid_user_id}")
    assert response.status_code == 200

    second_response = mocking_app.delete(f"/user/{valid_user_id}")
    assert second_response.status_code == 404


def test_delete_invalid_user_id_fails(mocking_app, invalid_user_delete_id):
    response = mocking_app.delete(f"/user/{invalid_user_delete_id}")
    assert response.status_code == 404


def test_put_user_returns_correct_result(mocking_app, sample_full_user_profile):
    user_id = 2
    response = mocking_app.put(f"/user/{user_id}", json=sample_full_user_profile.dict())

    assert response.status_code == 200


def test_put_user_twice_returns_correct_result(mocking_app, sample_full_user_profile):
    user_id = 2
    response = mocking_app.put(f"/user/{user_id}", json=sample_full_user_profile.dict())
    assert response.status_code == 200

    second_response = mocking_app.put(f"/user/{user_id}", json=sample_full_user_profile.dict())
    assert second_response.status_code == 200


def test_get_valid_user_id(mocking_app, valid_user_id):
    response = mocking_app.get(f"/user/{valid_user_id}")

    assert response.status_code == 200
    assert response.json()["short_bio"] == "default"
    assert response.json()["long_bio"] == "default"
    assert response.json()["username"] == "default"
    assert response.json()["liked_posts"] == []
