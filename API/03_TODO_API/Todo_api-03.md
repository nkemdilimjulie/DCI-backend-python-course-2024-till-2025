# Django API - ToDo - 3:  Consume an API with python

> Learning Goals
>- Consume Todo Api with Python
>- create a new traditional Django project with CustomUser
>- apply the restful Framework on top of this traditional Django project
>- create all CRUD endpoints with 2 Views


**Last Session**

- we created a restful crud todo API:
    - get ---> ListAPIView/ RetrieveAPIView
    - post ---> CreateAPIView
    - put/patch ---> UpdatedAPIView
    - delete ---> DestroyAPIView
- returns json formated data
- we consumed our API with
- we used `Postman` & `curl` (common line tool)
    - testing `API` endpoints
        - we can test with postman and curl all endpoints
- we used `javascript/react` to consume our API

### **Python Requests Example for Your API**

### Endpoints:

- **List all Todos**: `http://localhost:8000/api/`
- **Get a specific Todo by ID**: `http://localhost:8000/api/id`
- **Create a new Todo**: `http://localhost:8000/api/create`
- **Update a Todo by ID**: `http://localhost:8000/api/update/id`
- **Delete a Todo by ID**: `http://localhost:8000/api/delete/id`

Let's use the `requests` library to interact with your Django API.

#### **Create a Todo (POST request)**:
```python
import requests
import json

url = "http://localhost:8000/api/create/"
data = {
    "title": "Finish Homework",
    "body": "Complete the Python exercises"
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())
```

- This will send a POST request to create a new Todo. The `data` is serialized into JSON format.

#### **Update a Todo (PUT request)**:
```python
import requests
import json

url = "http://localhost:8000/api/update/1/"  # Update Todo with id 1
data = {
    "title": "Finish Homework - Updated",
    "body": "Complete the Python exercises and review concepts"
}

headers = {'Content-Type': 'application/json'}

response = requests.put(url, headers=headers, data=json.dumps(data))

print(response.json())
```

- This will update the `Todo` with `id=1`.

#### **Delete a Todo (DELETE request)**:
```python
import requests

url = "http://localhost:8000/api/delete/8"  # Delete Todo with id 1

response = requests.delete(url)

print(response.json())
```

- This sends a DELETE request to remove the Todo with `id=1`.

---