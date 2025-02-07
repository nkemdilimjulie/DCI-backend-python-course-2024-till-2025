# Todo API

we will build Todo API back-end that contains both a list API endpoint for all todos and dedicated endpoints for each individual todo. 

### Single Page Apps (SPAs)

SPAs are required for mobile apps that run on i0S or Android and is the dominant pattern for web apps that want to take advantage of JavaScript front-end frameworks/Libraries like `React, Vue, Angular`, and others.

There are multiple advantages to adopting a SPA approach. 

Developers can focus on their own area of expertise, typically either front-end or the back-end, but
rarely both. 

It allows for using testing and build tools suitable to the task at hand since building, testing, and deploying a Django project is quite different than doing the same for a JavaScript/React project.

And the forced separation removes the risk of coupling; it is not possible for front-end changes to break the back-end.

For large teams, SPAs make a lot of sense since there is already a built-in separation of tasks.

Even in smaller teams, the adoption cost of an SPA approach
is relatively small. 

The main risk of separating the back-end and the front-end is that it requires domain knowledge in both areas.

While Django is relatively
mature at this point the front-end ecosystem is decidedly not.

A solo developer should think carefully about whether the added complexity of a dedicated JavaScript front-end is worth it versus sprinkling JavaScript into existing Django templates with modern tools like:

- htmx (https://htmx.org/) or
- alpinjs (https://alpinejs.dev/)


### Initial Set Up

The first step for any Django APl is always to install Django and then later add Django REST Framework on top of it.

As usual create a folder then a virtual environment, activate it and install django:

```shell
mkdir todo && cd todo
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install django
```

Then create a traditional Django Project and add an app called todos and migrate:

```shell
(.venv) > django-admin startproject django_project .
(.venv) > python manage.py startapp todos
(.venv) > python manage.py migrate
```

add todos apps to our INSTALLED_APPS setting so do that now:

```python
# django_project/settings.py
INSTALLED_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib. sessions",
"django.contrib.messages", 
"django.contrib.staticfiles", 

# Local
"todos", # new
]
```

### .gitignore

 - add:
 1. .venv
 2. *.pyc
 3. database file

```shell
(.venv) > git add .
(.venv) > git commit -m "initial commit"
```

### Models

- defining the Todo database model within the todos app
- have only two fields: tit1le and body

```python
# todos/models.py
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
```

Since we have updated our model it’s time for Django’s  two-step migration:

```shell
(.venv) > python manage.py makemigrations todos
(.venv) > python manage.py migrate
```

It is optional to add the specific app we want to create a migration file for  - we could instead type just python manage.py makemigrations - however it is a good best practice to adopt. 

- you should strive to create a migration file for each small change.

If we had updated the models in two different apps and then run python manage.py makemigrations the resulting single migration file would contain data on both apps. 

That just makes debugging harder. 
Try to keep your migrations as small as possible.

### Admin

- add todo model to the admin interface:

```python
# todos/admin.py
from django.contrib import admin
from .models import Todo


admin.site.register(Todo)

```

Now we can create a superuser account to log in to the admin.

```shell
(.venv) > python manage.py createsuperuser
```


### Tests

We will use Django’s TestCase to create a test database and use
setUpTestData to create test data for our TodoModelTest class.

1. We want to confirm that the title and body appear as expected
2. We want to confirm that the __str__ method on the model works properly

```python
# todos/tests.py
from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
        title="First Todo",
        body="A body of text here"
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "First Todo")
        self.assertEqual(self.todo.body, "A body of text here")
        self.assertEqual(str(self.todo), "First Todo")
```

### Django REST Framework

add Django REST Framework:

```Shell
(.venv) > python -m pip install djangorestframework
```

### URLs

It is a good idea to have all API endpoints at a consistent path such as api/ in case you decide to add traditional Django webpages at a later date.

```python
# django_project/urls.py
from django.contrib import admin
from django.urls import path, include # new
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("todos.urls")), # new
]
```

Next create an app-level todos/urls.py file

```python
# todos/urls.py
from django.urls import path
from .views import ListTodo, DetailTodo
urlpatterns = [
path("<int:pk>/", DetailTodo.as_view(), name="todo_detail"),
path("", ListTodo.as_view(), name="todo_list"),
]
```

- referencing two views here
- There will be a list of all todos at the empty string " ", in other words at api/,
- each individual todo will be available at its primary key, pk (set by Django automatically)

The first entry is 1, the second is 2, and so on. 
Therefore our first todo will eventually be located at the API endpoint api/1/,the second  at api/2/,and so on.

### Serializers

There are two steps remaining: serializer and views.

the serializer transforms our model data into JSON that will be outputted at our desired URLs.

Create a new file called todos/serializers.py file:

```python
# todos/serializers.py
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
        "id",
        "title",
        "body",
        )
```

We're specifying which model to use and the specific fields on it we want to expose. 

Remember that id (similar to a pk) is created automatically by Django so we didn’t have to define it in our
Todo model but we will display in our individual detail view for each todo.

Django REST Framework will transform our data into JSON
exposing the fields for id, title, and body from our Todo model.

What's the difference between id and pk?

They both refer to a field automatically added to Django models by the ORM.

id is a built-in function from the Python
standard library while pk comes from Django itself. 

Generic class-based views like DetailView in Django expect to be passed a parameter named pk while on
model fields it is often common to simply refer to id.

The last thing we need to do is configure a views.py file to accompany our serializer and URLs.

### Views

We will use two DRF generic views here:

1. ListAPIView (return a collection )
2. RetrieveAPIView (return a resource)

```python
# todos/views.py
from rest_framework import generics
from .models import Todo 
from .serializers import TodoSerializer 

class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()[:2]
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
```

### Browsable API

Let’s use Django REST Framework’s browsable API now to interact with our data. Make sure the local server is running and navigate to
http://127.0.0.1:8000/api/ to see our working API list views endpoint.

This page shows the three todos we created earlier in the database model. An API endpoint refers to the URL used to make a request. If there are multiple items at
an endpoint it is known as a collection while a single item is known as a resource. The terms endpoint and resource are often used interchangeably by developers
but they mean different things.
We also made a DetailTodo view for each individual model which should be visible at:

- http://127.0.0.1:8000/api/1/.

You can also navigate to the endpoints for:
- http://127.0.0.1:8000/api/2
- http://127.0.0.1:8000/api/3
