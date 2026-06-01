def assert_status_code(response, expected_status_code):
    assert response.status_code == expected_status_code, (
        f"Expected Status code{expected_status_code}, "
        f"but got {response.status_code}. Response body:{response.body}"
    )



def assert_json_has_keys(data, required_keys):
    for key in required_keys:
        assert key in data, f"Missing expected key: {key}"

def assert_list_not_empty(data):
    assert isinstance(data, list), "expected response data to be a list"
    assert len(data)>0, "Expected response data length not be zero"

def assert_field_equals(data, field_name, expected_value):
    assert field_name in data, f"Missing expected field: {field_name}"
    assert data[field_name] == expected_value, (
        f"Expected {field_name} to be {expected_value}, "
        f"but got {data[field_name]}"
    )