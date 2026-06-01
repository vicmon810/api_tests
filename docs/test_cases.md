# Test Cases

| Test Case ID | Scenario | Steps | Expected Result |
|---|---|---|---|
| TC001 | Get user by valid ID | Send GET request to /users/1 | Status code is 200 and user ID is 1 |
| TC002 | Get all users | Send GET request to /users | Status code is 200 and response is a list |
| TC003 | Create post | Send POST request to /posts with valid payload | Status code is 201 and response contains created data |
| TC004 | Invalid user ID | Send GET request to /users/9999 | API returns 404 or empty object |
| TC005 | Invalid endpoint | Send GET request to /invalid-endpoint | Status code is 404 |