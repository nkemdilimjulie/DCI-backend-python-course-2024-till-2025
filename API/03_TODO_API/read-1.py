# - **List all Todos**: `http://localhost:8000/api/`
# - **Get a specific Todo by ID**: `http://localhost:8000/api/id`
# - **Create a new Todo**: `http://localhost:8000/api/create`
# - **Update a Todo by ID**: `http://localhost:8000/api/update/id`
# - **Delete a Todo by ID**: `http://localhost:8000/api/delete/id`

import requests

url_list = 'http://localhost:8000/api/'
url_detail = 'http://localhost:8000/api/1'

response = requests.get(url_list)
response = requests.get(url_detail)

print(response.json())