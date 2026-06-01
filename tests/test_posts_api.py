from utils.api_client import APIClient

client = APIClient("https://jsonplaceholder.typicode.com")

def test_create_post_success():
    payload = {
        "title" : "QA test",
        "body":"This is a test post",
        "userId": 1
    }

    response = client.post("/posts", payload)

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"]  == payload["body"]
    assert data["userId"]== payload["userId"]
    assert "id" in data