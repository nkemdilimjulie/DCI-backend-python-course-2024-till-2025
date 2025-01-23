# Django - Blog App - 01: Admin, View, Template, Model

> Learning Goals
>- Recap static, ListView, CSS
>- Primary Key and Foreign Key in django Models
>- User Table
>- DetailView
>- Parametrized urls/routes # mydomain.com/posts/my-post-title

**Last Session**

- complexer queries with Q

```python 
Post.objects.filter(Q(likes_gt=10) | Q(views_gt=15)) #  | --> OR
Post.objects.filter(~Q(likes_lt=2)) # ~ --> NOT
```

- aggregation: [1,2,3,4,5] ---reduce this---> 1 e.g. get the min of a collection of numbers
    - SUM(), AVG(), MAX(), COUNT()

```python 

from django.db.models import Count

Post.objects.aggregate(Count('like')) # return a dic
Post.objects.filter(text__icontains='Hello').aggregate(Count('like')) # How to count all likes from posts containing 'Hello'
Post.objects.filter(text__icontains='Hello').count()
Post.objects.values(title).annotate(views_sum=SUM("views"))  # QuerySet[{'title': 'Hello World', 'views_sum': 30}, {...}]
```

- Field Types:
    - CharField(max_length=255): limited amount of characters
    - TextField: unlimited field of characters
    - BigAutoField: we can make it a primary Key; each time a row is added to the table this field is incremented automatically;
        - (analog to serials in postgresql) 
        - type is integer
    - SlugField: stores slug strings: slug don't have white spaces and can only use character that are allowed in url
        - slug are usually unique labels for each entity in a list
        - human readable
        - /posts/hello_world_again
        - optimizes SEO; SEO is relevant for search engines 
    - DateTime: 
        - auto_now_add: create when a row (instance of my model) is add to the database 
        - auto_now: updates when a value of a row (instance of my model) is saved or updated
    - is_published = models.BooleanField
    - EmailField: checks the correct email syntax
    - ImageField: uploading images

# Blog App

- Build a Blog application with the following features:
    - Allow users to create, edit, and delete posts.
    - Display a homepage listing all blog posts.
    - Provide a dedicated page for each blog post.
- Use CSS for styling the application.

### Initial Set Up

1. make a new directory for our code called blog and go inside blog
2. create .venv and source it
3. pip install django
4. django-admin startproject django_project .
5. python manage.py startapp blog
6. migrate only
7. code .
8. add appname in setting

Let’s implement them now in a new command line terminal. Start with the new directory, a new virtual environment, and activate it.

```bash
$ mkdir blog
$ cd blog
$ python3 -m venv .venv
$ source .venv/bin/activate
$ (.venv)
(.venv) $ python -m pip install django
(.venv) § django-admin startproject django_project .
(.venv) $ python manage.py startapp blog
(.venv) $ python manage.py migrate
```

### Recap Databases

- **Database Overview**:
- A database is a place to store and access different types of data. There are two main types:
    - **Relational databases**.
    - **Non-relational databases**.

- **Relational Databases**:
    - Store information in **tables** made up of **columns** and **rows**, similar to an Excel spreadsheet.
    - **Columns** define what type of information can be stored (e.g., name, age, date).
    - **Rows** contain the actual data for each entry.
    - Frequently, data in separate tables are related, which gives these databases the name **“relational databases.”**
    - Best suited for:
        - Consistent, structured data.
        - Situations where relationships between entities (e.g., users and orders) are critical.

- **Non-relational Databases**:
    - Any database that doesn’t use the structured table format of relational databases.
    - Examples include:
        - Document-oriented databases (store data as JSON or XML documents). e.g. Mongo DB
        - Key-value stores (simple key-value pairs). e.g. redis
        - Graph databases (focus on relationships between data points).
        - Wide-column databases (store large-scale, column-oriented data).
    - Best suited for:
        - Unstructured or semi-structured data.
        - Scenarios where data size and shape must remain flexible.
        - Applications requiring adaptability to changes in the future.

### Django’s ORM
- ORM : Object-Relational Mapper
- makes working with data and relational databases much easier

- we don't have to worry about subtle differences in how each database interprets SQL.
- adds a layer of security: avoids SQL injects
- more readable;  we don’t have to write raw SQL ourselves. 
    - raw SQL is less readable
- In the case of Django, its ORM means we can write Python code to define database models;

- **Django ORM and Migrations**:
  - The Django ORM (Object-Relational Mapping) includes support for **migrations**.
  - Migrations help track and sync database changes over time, ensuring consistency.
  - This feature saves developers significant time and contributes to Django's efficiency.

- **Importance of Understanding Relational Databases**:
    - While the ORM abstracts much of the database interaction, a basic understanding of **relational databases** is necessary.
    - This knowledge ensures proper implementation and structuring of the database.

- Let’s look at how to structure the data in our Blog database.

So, for example, we could start with a table called “Post” with columns for the 
1. title, 
2. author, and 
3. body text. 

```shell

TITLE AUTHOR BODY
```

And the actual database table with columns and rows would look like this:

#### Post Database Table

```shell
TITLE                   AUTHOR  BODY
Getting Started         Piet    Welcome to my blog! This is my first post.
Today's Objectives      Piet    Dive into Django and create a functional blog app.
Reflections on Blogging Piet    Sharing thoughts and experiences as I write my 3rd post.

```

- To replicate the previous **Post** table using the Django ORM, add the following code to **blog/models.py**.

```python
# blog/models.py
from django.db import models
class Post(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()

    def __str__ (self):
        return self.title
```

  - To apply the new **Post** model to the database:
    1. Create a migration record using `python manage.py makemigrations`.
    2. Apply the migration with `python manage.py migrate`.

The database is now configured, and there is a new migrations directory within the blog app directory containing our changes.

### Primary Keys and Foreign Keys

1. Primary Key

- unique identifier
- Relational databases rely on relationships between tables to organize and manage data effectively.
- To facilitate communication between tables, a **primary key** column is added.
- It serves as a link to maintain consistent relationships between related tables.
- Primary keys are a fundamental part of relational database design.

- Django automatically adds an **auto-incrementing primary key** to every database model unless specified otherwise.
- The value of the primary key starts at 1 and increments sequentially (e.g., 2, 3, 4).

2. Foreign Key

- In a real blog application, users need to log in to create blog posts.
- This requires a second table for **users**, linked to the existing **Post** table for blog posts.

- Django provides a built-in authentication system that simplifies adding features like:
    - Signup, login, and logout.
    - Password reset and more.

- To link the **Post** table to the **User** table, the **author** field in the **Post** model must reference the **User model’s primary key (user_id)**.
- This type of relationship is called a **foreign key relationship**.
- It allows each blog post to have an **author** that corresponds to a user in the **User** table.

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE) # all posts that are related to specific user
                                                        # and this is deleted then all their associated posts will be
                                                        # deleted
    body = models.TextField()

    def __str__(self):
        return self.title
```

The ForeignKey field defaults to a many-to-one relationship, meaning one user can be the author of many different blog posts but not the other way around.

It is worth mentioning that there are three types of foreign relationships:

1. many-to-one,
2. many-to-many,
3. one-to-one.

- **Many-to-Many Relationship**:
    - Occurs when multiple entities in one table can be associated with multiple entities in another.
    - Example: A database tracking **authors** and **books**:
    - An author can write multiple books.
    - A book can have multiple authors.

- **One-to-One Relationship**:
    - Each entity in one table corresponds to exactly one entity in another table.
    - Example: A database tracking **people** and **passports**:
    - One person can have only one passport, and one passport belongs to only one person.

- **ForeignKey and `on_delete` Argument**:
    - `CASCADE`: Deletes the related objects.
    - `SET_NULL`: Sets the ForeignKey to `NULL` if the related object is deleted 

we should create a new migrations file and then migrate the database to apply it.

```Shell
(.venv) $ python manage.py makemigrations blog
(.venv) $ python manage.py migrate
```

### Views

In our views file, add the code below to display the contents of our Post model using ListView. 

It is quite rare that we use the default views.py code of
**from django.shortcuts import render** code that Django provides.

```python
# blog/views.py
from django.views.generic import ListView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

```

### Templates

we’ll start with a base.htm1 file and a home.html file that inherits from it. 

Then later, when we add templates for creating and editing blog posts, they too can inherit from base.html.

```shell
(.venv) $ mkdir templates 
```

Create two new templates 

templates/base.html and templates/home.html. 

And create the base.html template as follows.

```html
<!-- templates/base.html -->
<html>
<head>
<title>Django blog</title>
</head>
<body>
<header>
<h1><a href="{% url 'home' %}">Django blog</a></h1>
</header>
<div>
{% block content %}
{% endblock content %}

</div>
</body>
</html>
```

home.html.

```html
<!-- templates/home.html -->
{% extends "base.html" %}
{% block content %}
{% for post in post_list %}
<div class="post-entry">

<h2><a href="">{{ post.title }}</a></h2>

<p>{{ post.body }}</p>
</div>
{% endfor %}
{% endblock content %}
```

### Individual Blog Pages

Start with the view. We can use the generic class-based DetailView to simplify things. 
At the top of the file, add DetailView to the list of imports and then create a new view called BlogDetailView.

```python
# blog/views.py
from django.views.generic import ListView, DetailView # new
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView): # new
    model = Post
    template_name = "post_detail.html"
```

- we define the model we're using, Post
- we define the template we want it associated with, post_detail.html.

Create a new template file for a post detail called templates/post_detail.html:

```html
<!-- templates/post_detail.html -->
{% extends "base.html" %}
{% block content %} 
<div class="post-entry"> 
    <h2>{{ post.title }}</h2>
    <p>{{ post.body }}</p>
</div> 
{% endblock content %} 
```

- this template inherits from base.html.
- display the title and body from our context object (here it is post; DetailView makes accessible as post.) 

Add a new URL path for our view, which we can do as follows.

```python
# blog/urls.py
from django.urls import path
from .views import BlogListView, BlogDetailView # new
urlpatterns = [
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"), # new
    path("", BlogListView.as_view(), name="home"),
]
```
All blog post entries will start with post/.

- Each post entry is represented by an auto-incrementing primary key, which is an integer (`<int:pk>`).
- The primary key (PK) for the first post, "Hello, World," is `1`.
- The PK for the second post is `2`, and so on.
- For the individual entry page of the first post, the URL pattern will be `post/1/`.