import json


def test_create_user(client):
    data = {
        "email": "test@fastapi.com",
        "username": "test",
        "password": "test_fastapi@2486",
        "is_superuser": True
    }

    response = client.post("/api/v1/user/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "test@fastapi.com"
    assert response.json()["is_active"] is True
    assert response.json()["is_superuser"] is True


def test_fetch_user(client):  # new test
    data = {
        "email": "test@fastapi.com",
        "username": "test",
        "password": "test_fastapi@2486",
        "is_superuser": True
    }

    response = client.post("/api/v1/user/", json.dumps(data))
    response = client.get("/api/v1/user/1")
    assert response.status_code == 200
    assert response.json()['username'] == "test"


def test_fetch_users(client):  # new test
    data_1 = {
        "email": "test1@fastapi.com",
        "username": "test1",
        "password": "test1_fastapi@2486",
        "is_superuser": True
    }
    data_2 = {
        "email": "test2@fastapi.com",
        "username": "test2",
        "password": "test2_fastapi@2486",
        "is_superuser": False
    }

    response = client.post("/api/v1/user/", json.dumps(data_1))
    response = client.post("/api/v1/user/", json.dumps(data_2))
    response = client.get("/api/v1/user/")
    assert response.status_code == 200


def test_delete_user(client):
    data = {
        "email": "test@fastapi.com",
        "username": "test",
        "password": "test_fastapi@2486",
        "is_superuser": True
    }

    response = client.post("/api/v1/user/", json.dumps(data))
    response = client.delete("/api/v1/user/1")
    assert response.status_code == 200


def test_update_user(client):
    data = {
        "email": "test@fastapi.com",
        "username": "update_test",
        "password": "test_fastapi@2486",
        "is_superuser": True,
    }
    update_data = {
        "email": "test@fastapi.com",
        "username": "update_test",
        "is_active": False
    }

    response = client.post("/api/v1/user/", json.dumps(data))
    response = client.put("/api/v1/user/1", json.dumps(update_data))
    assert response.status_code == 200
    # assert response.json()['username'] == "update_test"
    # assert response.json()['is_active'] is False
