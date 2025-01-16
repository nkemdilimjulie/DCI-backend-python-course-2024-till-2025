# Django - Message Board App - 01: Model & Admin interface

Thanks to the powerful Django ORM (Object-Relational Mapper), there
is built-in support for multiple database backends: 

1. PostgreSQL
2. MySQL
3. MariaDB
4. Oracle
5. SQLite

As a result, developers can write the same Python code in a models.py file, which will automatically be translated into the correct SQL for each database. 

The only configuration required is to update the DATABASES section of our django_project/settings.py
file.


For local development, Django defaults to using SQLite

## Setup

```bash
mkdir message-board
cd message-board
$ python3 -m venv .venv

$ source .venv/bin/activate
$ (.venv)

(.venv) $ python -m pip install django

(.venv) § django-admin startproject django_project .
(.venv) $ python manage.py startapp posts
```

As a final step, update **django_project/settings.py** to alert Django to
the new app, posts, by adding it to the bottom of the INSTALLED_APPS
section.

Then execute the migrate command to create an initial database based on
Django’s default settings.

```shell
(.venv) $ python manage.py migrate
```

### Create a Database Model

Our first task is to create a database model where we can store and display
posts from our users. 

Django’s ORM will automatically turn this model into
a database table for us.
In a real-world Django project, there are often many complex, interconnected database models, but we only need one in our simple
message board app.

Open the posts/models.py file and look at the default code which Django
provides:

```python
# posts/models.py
from django.db import models
# Create your models here
```

Django imports a module, models, to help us build new database models
which will “model” the characteristics of the data in our database.

For each database model we want to extend django.db.models.Model and then add our fields.
To store the textual content of a message board post, we can do the following:

```python
# posts/models.py
from django.db import models
class Post(models.Model): # new

    text = models.TextField()
```

Activating Post Model:

From now on, whenever we make or modify an existing model, we’ll need to update Django
in a **two-step process**:

1. First, we create a migrations file with the makemigrations command.
Migration files create a reference of any changes to the database models,
which means we can track changes-and debug errors as necessary-over
time.

*python manage.py makemigrations posts* 
```bash
.
├── db.sqlite3
├── django_project
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── posts
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   ├── 0001_initial.py
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py

```

2. Second, we build the database with the migrate command, which
executes the instructions in our migrations file.

*python manage.py migrate*

- Create model Post

```bash
(.venv) $ python manage.py migrate posts
Operations to perform:

Apply all migrations: admin, auth, contenttypes, posts,
sessions
Running migrations:

Applying posts.0001_initial... OK

```

You don’t have to include a name after makemigrations. 
If you just run makemigrations without specifying an app, a migrations file will be
created for all available changes throughout the Django project. 
That is fine in a small project like ours with only a single app, but most Django projects
have more than one app!
Therefore if you made model changes in multiple apps, the resulting migrations file would include all those changes: not ideal! 


Migrations files should be as small and concise as possible, making it easier 
to debug in the future or even roll back changes as needed.

Therefore, as a best practice, adopt the habit of always including the name of an app when 
executing the makemigrations command!

### Django Admin

One of Django’s killer features is its robust admin interface that visually interacts with data. 

It came about because Django started off as a newspaper CMS (Content Management System). 

The idea was that journalists could write and edit their stories in the admin without needing to touch “code.” 

Over time, the built-in admin app has evolved into a fantastic, out-of-the-box tool for managing all aspects of a Django project.

To use the Django admin, we must first create a superuser who can login.

In your command line console, type **python manage.py createsuperuser**
and respond to the prompts for a username, email, and password:

```Shell
(.venv) $ python manage.py createsuperuser
Username (leave blank to use 'wsv'): piet
Email: bla@bla.com
Password:
Password (again):

Superuser created successfully.
```

Are posts are not displayed in the Django Admin Interface.
Just as we must explicitly add new apps to the INSTALLED_APPS config, so,
too, must we update an app’s admin.py file for it to appear in the admin.

In your text editor, open up posts/admin.py and add the following code to
display the Post model.

```python
# posts/admin.py
from django.contrib import admin
from .models import Post
admin.site.register(Post)
```

Django now knows it should display our posts app and its database model
Post on the admin page. If you refresh your browser, you'll see that it
appears.

We can save data via our Django interface be add Text and click the save button.
however, if you look closely, there’s a problem: our new entry is called “Post object (1)”,
which isn’t very descriptive!

Within the posts/models.py file, add a new method called str, which provides a human-readable representation of the model. 

In this case, we’ll have it display the first 50 characters of the text field.

```python
# posts/models.py
from django.db import models
class Post(models.Model):
    text = models.TextField()

    def __str__ (self): # new
        return self.text[:50]
```

If you refresh your Admin page in the browser, you'll see it's changed to a
much more descriptive and helpful representation of our database entry.