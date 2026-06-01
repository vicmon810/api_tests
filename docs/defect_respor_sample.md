# Defect Report Sample

## Title
Invalid user endpoint returns empty object instead of clear error message

## Environment
API: JSONPlaceholder  
Endpoint: GET /users/9999  
Tool: pytest + requests  

## Steps to Reproduce
1. Send GET request to /users/9999
2. Check response status code
3. Check response body

## Expected Result
The API should return a clear 404 response with an error message.

## Actual Result
The API returns an empty JSON object.

## Severity
Low

## Notes
This may be acceptable for a mock API. However, in a production system, a clear error message would improve debugging and traceability.