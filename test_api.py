import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user():
    response = requests.get(
        f"{BASE_URL}/users/1",
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)

    assert "id" in data
    assert "name" in data
    assert "username" in data
    assert "email" in data

    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["username"], str)
    assert isinstance(data["email"], str)

    assert data["id"] == 1


def test_create_user():
    user_data = {
        "name": "Ivan Ivanov",
        "username": "ivan",
        "email": "ivan@example.com"
    }

    response = requests.post(
        f"{BASE_URL}/users",
        json=user_data,
        timeout=10
    )

    assert response.status_code == 201

    data = response.json()

    assert isinstance(data, dict)

    assert "id" in data
    assert "name" in data
    assert "username" in data
    assert "email" in data

    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["username"], str)
    assert isinstance(data["email"], str)

    assert data["name"] == "Ivan Ivanov"
    assert data["username"] == "ivan"
    assert data["email"] == "ivan@example.com"


def test_update_user():
    user_data = {
        "id": 1,
        "name": "Ivan Petrov",
        "username": "ivan_petrov",
        "email": "petrov@example.com"
    }

    response = requests.put(
        f"{BASE_URL}/users/1",
        json=user_data,
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)

    assert "id" in data
    assert "name" in data
    assert "username" in data
    assert "email" in data

    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["username"], str)
    assert isinstance(data["email"], str)

    assert data["id"] == 1
    assert data["name"] == "Ivan Petrov"
    assert data["username"] == "ivan_petrov"
    assert data["email"] == "petrov@example.com"