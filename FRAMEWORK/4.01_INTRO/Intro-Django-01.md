# Frameworks - Introduction 01: Django

> Learning Goals
>- Overview Framework
>- Setup Django and create a Hello World app
>- virtual environment (recap)
>- git (recap)
>- talking World Wide Web
>- Model View Controller vs. MVT(U)

**What is Django?**

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

- Open-source web framework for backend web applications based on Python.
- Excels at creating websites that can handle high amounts of traffic and transactions.

## Key Features of Django:

**Batteries-Included Philosophy**:

- This means it provides everything developers need to build a web application from start to finish
- no need to rely on external libraries for core functionality.

**ORM (Object-Relational Mapping)**:
- it that abstracts the process of working with databases
- Instead of writing raw SQL queries, developers define the structure of the database using Python classes

**Automatic Admin Interface**:
- One of Django's most powerful features
- Given the structure of your database, Django can automatically generate a sophisticated admin interface

**Security**:
- Django provides built-in protection against many common web attacks, such as Cross Site Scripting (XSS), Cross Site Request Forgery (CSRF), and SQL Injection.


**Migration System**:
- Allows developers to change the structure of the database over time without having to recreate it from scratch

**Extensibility**: 
- Django is designed to be highly extensible.
- It has a robust system of 'apps' that can be plugged into a project.
- This modular approach lets developers reuse components across multiple projects.

## Why Use Django?
**Rapid Development**
**Highly Scalable**
**Huge Community**
**Mature and Robust**

**What is Framework?**

- serves as a template with predefined functionalities
- increases development of web apps
- it's like a swiss army knife
- aids the development of web applications and web APIs
- provides libraries for database access, templating, session management, and more

#### Front-end

JavaScript
- ReactJS
- Angular
- VueJS

CSS (Cascade Style Sheet) (style sheet language/ declarative language)
- Tailwind CSS
- Bootstrap
- Materialize

#### Back-end

Python
- Django
- Cherry Pie
- Flask

Javascript
- Express.js
- Next.js

Ruby
- Ruby on Rails

PHP
- Laravel
- Symphony
- CodeIgniter

# Setup

What is a virtual env?
- isolated environment
- manage dependencies (libraries, packages, tools)
- not affecting other projects or the global Python installation

Why do we need it?
- Project Isolation
- Prevent Dependency Conflicts
- Reproducibility (requirements.txt)
- Cleaner Global Installation

- Safety:
    - Avoid accidental changes to global or system-level Python installations, which might be critical for the operating system

1. 1. Create Virtual environment:

```bash
python3 -m venv .venv
```

1. 2. Activate Virtual environment 
```bash
source .venv/bin/activate
```

2. Initialize git repository
```bash
git init
```

3. Ignore your virtual environment
add `/.venv/` to `.gitignore` file.

4. Install Django

```pip install django```

# Creating a project

`django-admin startproject django_project .`

that command will create the following folder structure:

```bash
├── django_project
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

**`manage.py`**:
- A command-line utility that allows you to interact with your project in various ways 
    - start djangos dev server
    - running tests
    - create migrations and migrate
    - discard our data from our database
    - load data into our database
- executes various Django commands

**`__init__.py`**:
- indicates that the files in the folder are part of a Python package. 
- Without this file, we cannot import files from another directory which we will be doing a lot of in Django!

**`asgi.py`**:
- Stands for Asynchronous Server Gateway Interface.
- An interface between web servers and web applications.
- handles asynchronous requests
- can be optional run
- needs to handle tasks or interactions that involve non-blocking operations
- Real-time messaging apps (chats)
- Instant alerts or updates
- Video or audio streams

**`settings.py`**:
- Contains settings for your Django project.
- This is where you'll define database configurations, static and media files handling, installed apps, middleware, templates settings, etc.


**`urls.py`**:
- Contains the URL declarations for the Django project.
- It's essentially a table of contents for your app, where you define URL patterns and associate them with view functions or classes.
- Think of it as a map or router for incoming web requests.

**`wsgi.py`**:
- Stands for Web Server Gateway Interface.
- An interface between web servers and web applications.

**starting project:**

`python manage.py runserver`

- go to the localhost:8000 
- you will see the landing page

**migrate**

- It is safe to ignore the warning about 18 unapplied migrations at this point. 
- Django is complaining that we have not yet 'migrated' our initial database. 
- we can remove it by first stopping the local server with the command
Control+c and then running 

`python manage.py migrate`

- What Django has done here is create a SQLite database and migrated its built-in apps provided for us.
- This is represented by the new db.sqlite3 file in our directory.

**starting project again:**

`python manage.py runserver`


### Create An App

- django uses the concept of projects and apps to keep the code clean and readable
- a singe top-level Django project can contain multiple apps
- each app controls an isolated piece of functionality
- each app should have a clear function

to create an app run:

`python manage.py startapp pages`

this will generate the following folder structure:
```bash
└── pages
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
```

### Adding the App to our project:

1. add `pages` to INSTALLED_APPS in settings.py
2. create a view function in `pages/views.py`
3. create a file named urls.py in the pages directory
4. add the pages url to `django_project/urls.py`


### Saving Project related Dependencies: requirements.txt

We want a record of packages installed in our virtual environment.
The current bes practice is to create a requirement.txt file with this information.

`pip freeze > requirments.txt`

### Loading the requirements.txt

When other devs clone your repo, the can use the requirements.txt to install all packages:

`pip install -r requirements.txt`

## Your First View

- For our first website we'll create a Web page that outputs the text “Hello, World!”
- This is a static page that does not involve a database or even a templates file.

- Instead, it is a good introduction to how views and URLs work within Django.

- A view is a Python function that accepts a Web request and returns a Web response.

1. The response can be the HTML
contents of a Web page,
2. a redirect,
3. a 404 error
4. an image
5. or really anything.


- When a Web page is requested, 
- Django automatically creates an HttpRequest object that contains metadata about the
request.
- HttpRequest are the first arguments of view function.
- the view function returns an HttpResponse object

- lets look at our view:

```python
from django.shortcuts import render
```

`render()` is a Django shortcut function that can be used to create views
however there is an even simpler approach possible
which we will use instead: the built-in `HttpResponse method`

Update the pages/views.py file with the following code:

```python
# pages/views.py
from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse("Hello, World!")
```

-  the view returns an Http Response object with the string of text “Hello, World!”


### URLconfs

update it with the following code: 

```python
# pages/urls.py

from django.urls import path
from .views import home_page_view

urlpatterns = [
    path('', home_page_view, name='my_home'),
]
```

By referring to the views.py file as .views we are telling Django to look within the current directory for a views.py file and
import the view home_page_view from there.

Our URL pattern here has three parts:
- the empty string, ""
- a reference to the view called home_page_view
- an optional named URL pattern called "my_home" (target name of a url)

- if the user requests the homepage represented by the 
empty string '', Django should use the view called home_page_view.

- then we “include” URLs from our individual apps (page) in the main project url:

```python
# django_project/urls.py
from django.contrib import admin
from django.urls import path, include # new


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('pages.urls')), # new
]
```

Now whenever a user visits the homepage-represented by the empty string here, ' ', they will be routed to the URLs file in
the pages app.

Think of the top-level django_project/urls.py as the gateway to various URL patterns distinct to each app.

we started our django server:

```python manage.py runserver```

If you refresh the browser for http://127.0.0.1:8000/ 
it now displays the text “Hello, World!”

### Git

1. stage your changes: 
2. commit
3. publish on github