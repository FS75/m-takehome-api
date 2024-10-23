# m-takehome-app

Link to the API: \
https://m-takehome-api-45652458453.us-central1.run.app/

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | / | Retrieve all objects (added this endpoint in for ease of viewing all objects) |
| GET    | /{id} | Retrieve object by ID |
| POST   | / | Create a new object |
| DELETE | /{id} | Delete object by ID |

## Example POST Request body

```json
{
    "id": "4",
    "full_name": "xyz",
    "email": "xyz@abc.com",
    "mobile_number": "12321231"
}
