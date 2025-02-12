# - **Create a new Todo**: `http://localhost:8000/api/create`
# - **Update a Todo by ID**: `http://localhost:8000/api/update/id`
# - **Delete a Todo by ID**: `http://localhost:8000/api/delete/id`

import requests
import json

url = 'http://localhost:8000/api/create/'
data = {
    'title': 'hello from python',
    'body': 'lorem again new'
}

response = requests.post(
    url,
    headers={'Content-Type': 'application/json'},
    data=json.dumps(data)
)

print(response.json())
# print(response.encoding)


#--------Version 2


import requests

url = 'http://localhost:8000/api/create/'
data = {
    'title': 'hello from python',
    'body': 'lorem again new'
}

response = requests.post(
    url,
    json=data
)

print(response.json())