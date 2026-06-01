from utils.api_client import APIClient
from utils.assertions import (
    assert_status_code,
    assert_json_has_keys,
    assert_list_not_empty,
    assert_field_equals
)

client = APIClient("https://jsonplaceholder.typicode.com")

def test_get_user_by_valid_id():
    response = client.get("/users/1")

    # assert response.status_code == 200
    assert_status_code(response, 200)
    data = response.json()

    # assert data["id"] == 1
    # assert "name" in data 
    # assert "email" in data 
    # assert "company" in data
    # 

    assert_json_has_keys(data, ["id", "name", "email", "company"]) 
    assert_field_equals(data, "id",1)

def test_get_all_user_returns_list():
    response = client.get("/users")

    # assert response.status_code == 200
    assert_status_code(response, 200)

    data = response.json()

    # assert isinstance(data, list)
    # assert len(data) > 0 
    # assert "id" in data[0]
    # assert "email" in data[0]

    assert_list_not_empty(data)
    assert_json_has_keys(data[0], ["id","name","email"])

