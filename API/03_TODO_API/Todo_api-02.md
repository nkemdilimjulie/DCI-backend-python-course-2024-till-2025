# Django API - 2: CRUD API & Consume an API

> Learning Goal
>- Continue with writing test for ToDo APi
>- add rest of our CRUD endpoints
>- Consume this API (our Django ToDo API )
    >- curl
    >- Postman
    >- python with the `requests` lib
    >- javascript/react with `axios` lib


**Last Session**

- serializer:
    - transform (serialize) python objects into json format 
    - we extend the ModelSerializer
    - for configuring the serializer an inner Mete class is used for serializer Class
- Views
    - extended the ListAPIView
    - extended the RetrieveAPIView

```python
from .models import Todo

class ListTodo(ListAPIView):
    queryset = Todo.objects.all()[:2]
    serializer_class = TodoSerializer

class DetailTodo(RetrieveAPIView):
    queryset = Todo.objects.all()[:2]
    serializer_class = TodoSerializer
```

- SPA: Single Page Application
    - on the first site visit most of all assets and static files and html/jsx files are loaded
    - when I go to another page of this SPA less loading is required
        - this increases performance and user experience
    - to use SPA we have to completely separate the backend from the frontend 

### API TESTS

This time there are two pages to test:
- collection endpoint
- single resource endpoint

```python
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Todo

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title='First Todo',
            body='A body'
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, 'First Todo')
        self.assertEqual(Todo.objects.get(id=1).title, 'First Todo')
        self.assertEqual(self.todo.body, 'A body')
        self.assertEqual(str(self.todo), 'First Todo')

    def test_api_listview(self):
        response = self.client.get(
                    reverse('todo_list'),
        )
        self.assertEqual(response.status_code, 
                status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "First Todo")
        self.assertContains(response, "A body")

    def test_api_detailview(self):
        response = self.client.get(
            reverse(
                "todo_details", 
                kwargs={'pk': self.todo.id},
                )
        )
        self.assertEqual(response.status_code, 
                status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "First Todo")
        self.assertContains(response, "A body")

```

### Full CRUD
#### Views
we have to add:

- CreateTodo(`CreateAPIView`)
- UpdateTodo(`UpdateAPIView`)
- DeleteTodo(`DestroyAPIView`) 

```python
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Todo
from .serializers import TodoSerializer

.......


# NEW
class CreateTodo(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class UpdateTodo(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DeleteTodo(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
```

**CreateTodo (CreateAPIView)**
When someone sends a `POST` request to `/create/` with new `Todo` data (like title and description), this view will save the new `Todo` in the database and return a success response with the created `Todo`.

 **UpdateTodo (UpdateAPIView)**
When someone sends a `PUT` request to `/update/{id}/` (where `{id}` is the `Todo`'s ID) with new data, this view will update the existing `Todo` and return the updated data.

**DeleteTodo (DestroyAPIView)**
 When someone sends a `DELETE` request to `/delete/{id}/` (where `{id}` is the `Todo`'s ID), this view will delete the specific `Todo` and return a success message or status.

 #### Urls

```python
from django.urls import path
from .views import ListTodo, DetailTodo, CreateTodo, UpdateTodo, DeleteTodo

urlpatterns = [
    path("", ListTodo.as_view(), name="todo_list"),
    path("<int:pk>/",  DetailTodo.as_view(), name="todo_details"),
    #NEW
    path("create/", CreateTodo.as_view(), name="todo_create"),
    path("update/<int:pk>/", UpdateTodo.as_view(), name="todo_update"),
    path("delete/<int:pk>/", DeleteTodo.as_view(), name="todo_delete"),

]

```

- **`path("create/", CreateTodo.as_view(), name="todo_create")`**
   - This endpoint allows us to create a new `Todo` object by sending a `POST` request with data like `title` and `body`.

-  **`path("update/<int:pk>/", UpdateTodo.as_view(), name="todo_update")`**
   - This endpoint allows us to update an existing `Todo`.
   - `<int:pk>` captures the `id` (primary key) of the `Todo` that we want to update.   

- **`path("delete/<int:pk>/", DeleteTodo.as_view(), name="todo_delete")`**
   - This endpoint allows us to delete a specific `Todo`.
   - `<int:pk>` captures the `id` (primary key) of the `Todo` that we want to delete.


### Consuming our Django restful API

### Endpoints:

- **List all Todos**: `http://localhost:8000/api/`
- **Get a specific Todo by ID**: `http://localhost:8000/api/id`
- **Create a new Todo**: `http://localhost:8000/api/create`
- **Update a Todo by ID**: `http://localhost:8000/api/update/id`
- **Delete a Todo by ID**: `http://localhost:8000/api/delete/id`


### **CRUDE Operations**
- **CREATE** - POST: Create a new Todo item.
- **READ** - GET: Retrieve all or specific Todo items.
- **UPDATE** - PUT or PATCH: Update an existing Todo item.
- **DELETE** - DELETE: Remove a Todo item.

### Consumin with Curl

```bash
# 1. Fetch the list of all todos (GET)
curl -i http://localhost:8000/api/

# 2. Fetch a specific todo (GET with id=1)
curl -i http://localhost:8000/api/1/

# 3. Create a new todo (POST)
curl -X POST -i http://localhost:8000/api/create/ \
  -H "Content-Type: application/json" \
  -d '{"title": "New Todo", "body": "This is a newly created Todo item."}'

# 4. Update a specific todo (PUT with id=1)
curl -X PUT -i http://localhost:8000/api/update/1/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Todo Title", "body": "Updated content for the Todo item"}'

# 5. Delete a specific todo (DELETE with id=1)
curl -X DELETE -i http://localhost:8000/api/delete/1/
```


### Curl flags
```bash
curl -i http://localhost:8000/api/
```
- This will return a list of all Todo items. The `-i` option includes both the HTTP headers and the response body.

```bash
curl -I http://localhost:8000/api/
```
- The `-I` option fetches only the HTTP headers without the response body.

```bash
curl -o todo_list_output.txt http://localhost:8000/api/
```
- This saves the response body to a file named `todo_list_output.txt`.

```bash
curl -O http://localhost:8000/api/
```
- The `-O` option will save the file as `api` (or another name depending on the URL).


### Consuming with Postman

Postman is a great tool for testing APIs.

1. **Create an Account**: Create a Postman account if you don't already have one.
2. **Create a New Workspace**: Start by creating a new workspace to organize your requests.
3. **Create a New Request**:
   - **GET Request**: Use this method to fetch data from your API (list all Todos or a specific Todo).
   - **POST Request**: Use this method to send data to the server and create a new Todo.
   - **PUT Request**: Use this method to update an existing Todo.
   - **PATCH Request**: Use this method to update an existing Todo.
   - **DELETE Request**: Use this method to delete a Todo by its ID.

### Consume by Javascript/React Frontend



### **Overview:**
- We're building a full-stack application, where the **backend** is powered by Django (providing the API) and the **frontend** is built using React (consuming the API).
- The backend exposes data (such as a list of todos) through an API, and the frontend interacts with that API to display and manipulate the data.
  
In this setup, **React** is making requests to your **Django API** using **HTTP requests** (like GET, POST) and displaying the data to the user. The backend handles the actual logic, like creating, retrieving, updating, and deleting data in the database, and the frontend presents that data in a user-friendly way.

### **Frontend Components:**

#### **1. `ListView` Component:**
This is the part of the application that displays all the todos.

- **Fetching Data from the Backend (GET request):**
  ```jsx
  useEffect(() => {
    axios.get('http://localhost:8000/api/')
      .then((response) => {
        setTodos(response.data);
        console.log(response.data);
      })
      .catch((error) => {
        console.error('Error fetching todos:', error);
      });
  }, []);
  ```
  - **How this works**: When the `ListView` component is first loaded, it makes a **GET request** to the Django API (`http://localhost:8000/api/`) to fetch all the todos.
  - **Backend Role**: The Django backend processes this request and sends back a response with all the todos in the database.
  - **Frontend Role**: The frontend receives this data, stores it in a `todos` state variable using `useState`, and then renders it in an unordered list (`<ul>`). Each todo is displayed with a clickable title (`<Link>`) that takes the user to a detailed view of the todo.

- **Displaying the Todos:**
  ```jsx
  <ul>
    {todos.map((todo, index) => (
      <li key={todo.id}>
        <Link to={`/${todo.id}`}>
          <h3>{todo.title}</h3>
        </Link>
        <p>{todo.body}</p>
      </li>
    ))}
  </ul>
  ```
  - The `todos` array is mapped over to display each todo in a list. The `todo.id` is used as a unique key for each list item.
  - **Linking to the Detail View**: When the user clicks on a todo title, they are directed to a detailed view of that specific todo (using `Link` from `react-router-dom`).

#### **2. `DetailView` Component:**
This component shows the details of a specific todo when the user clicks on it.

- **Fetching Data for a Specific Todo (GET request):**
  ```jsx
  useEffect(() => {
    axios.get(`http://localhost:8000/api/${id}/`)
      .then((response) => {
        console.log(response.data);
        setTodo(response.data);
      })
      .catch((error) => {
        console.error('Error fetching todo details:', error);
      });
  }, [id]);
  ```
  - **How this works**: When the user clicks on a todo title in `ListView`, they are taken to `DetailView`, where the `id` of the selected todo is extracted from the URL using `useParams()` from `react-router-dom`.
  - **Backend Role**: The Django backend receives the `GET` request for the specific todo with `id=1`, for example, and sends the details of that todo back.
  - **Frontend Role**: The frontend receives the details of the selected todo and displays them.

- **Displaying the Todo Details:**
  ```jsx
  return (
    <div>
      <h1>{todo.title}</h1>
      <p>{todo.body}</p>
    </div>
  );
  ```
  - The title and body of the todo are rendered once the data is successfully fetched from the backend.

#### **3. `CreateTodo` Component:**
This component allows the user to create a new todo by sending data to the backend.

- **Submitting a New Todo (POST request):**
  ```jsx
  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://localhost:8000/api/create/', { title, body })
      .then((response) => {
        console.log('Todo created:', response.data);
        navigate('/');
      })
      .catch((error) => {
        console.error('Error creating todo:', error);
      });
  };
  ```
  - **How this works**: When the user fills out the form to create a new todo, the data (title and body) is sent to the Django API using a **POST request**.
  - **Backend Role**: The Django backend processes the request and creates a new todo in the database, returning the created todo data.
  - **Frontend Role**: Once the new todo is created, the frontend redirects the user back to the main list of todos using `navigate('/')`.

- **Creating the Form:**
  ```jsx
  <form onSubmit={handleSubmit}>
    <input
      type="text"
      value={title}
      onChange={(e) => setTitle(e.target.value)}
      placeholder="Enter todo title"
    />
    <textarea
      value={body}
      onChange={(e) => setBody(e.target.value)}
      placeholder="Enter todo body"
    />
    <button type="submit">Create</button>
  </form>
  ```
  - The form allows the user to enter a title and body for the new todo, and when the form is submitted, the data is sent to the Django API to create the new todo.

### **How the Backend (Django API) is Used in the Frontend (React):**

1. **GET Requests**: The frontend makes **GET requests** to the Django API to fetch data (like all todos or details of a specific todo).
   - **Frontend**: React uses `axios` to send the requests and handle the responses.
   - **Backend**: Django receives the requests, processes them, interacts with the database, and sends back the data (as JSON).

2. **POST Requests**: The frontend sends **POST requests** to create new resources (like a new todo).
   - **Frontend**: React sends the data (title and body) to the backend.
   - **Backend**: Django processes the data, creates a new record in the database, and responds with the newly created todo.

3. **Linking Backend and Frontend**: React is essentially **consuming** the backend's API. The backend provides the data, and the frontend (React) interacts with it by sending requests and displaying the data.
