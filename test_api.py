import requests

def test_get_user_status_code():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200

def test_get_user_name():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.json()["name"] == "Leanne Graham"

def test_get_user_email():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.json()["email"] == "Sincere@april.biz"

def test_get_user_city():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.json()["address"]["city"] == "Gwenborough"

def test_get_user2_name():
    response = requests.get("https://jsonplaceholder.typicode.com/users/2")
    assert response.json()["name"] == "Ervin Howell"
    assert response.json()["name"] == "Ervin Howell", \
        f"Expected Ervin Howell, got {response.json()['name']}"


def test_get_user999_status_code():
    response = requests.get("https://jsonplaceholder.typicode.com/users/999")
    assert response.status_code == 404
