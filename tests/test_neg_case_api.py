from utils.api_client import APIClient

client = APIClient("https://jsonplaceholder.typicode.com")

def test_get_invalid_user_id():
    response = client.get("/users/34dfiiiif")
    assert response.status_code == 404 or response.json() == {}

def test_get_invalid_endpoint():
    response = client.get("/invalid_endpoint")

    assert response.status_code == 404

    