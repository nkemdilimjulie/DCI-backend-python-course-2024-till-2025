# - **Create a new Todo**: `http://localhost:8000/api/create`
# - **Update a Todo by ID**: `http://localhost:8000/api/update/id`
# - **Delete a Todo by ID**: `http://localhost:8000/api/delete/id`

import requests

# url = 'http://localhost:8000/api/update/17/'
# data = {
#     'title': 'hello from python update',
#     'body': 'lorem again update'
# }

# response = requests.put(
#     url,
#     headers={'Content-Type': 'application/json'},
#     json=data
# )

# print(response.json())

data = {
    'title': 'hello from python update',
}

response = requests.patch(
    url,
    headers={'Content-Type': 'application/json'},
    json=data
)

print(response.json())