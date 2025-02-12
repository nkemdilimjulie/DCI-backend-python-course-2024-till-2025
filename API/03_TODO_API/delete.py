# - **Delete a Todo by ID**: `http://localhost:8000/api/delete/id`

import requests

url = 'http://localhost:8000/api/delete/16/'

response = requests.delete(
    url,
)

print(response)