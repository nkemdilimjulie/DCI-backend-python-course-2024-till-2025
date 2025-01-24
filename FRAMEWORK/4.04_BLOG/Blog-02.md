Django - Blog App - 02: Statics, DetailView & Tests

> Learning Goals
>- adding a method to models: get_absolute_url
>- DetailView vs. function based View vs. TemplateView
>- Recap of statics
>- Testing

**Last Session**
- Databases:
    - relational
    - non-relational

How relationships are formed in a relational database: 
- We can establish relationships between 2 Tables by using Foreign Key and Primary Key

Parent Tabel

id (primary Key) name
1                 bob
2                 tony

we have unique entries in name columns

Child tabel

id  name     parent_id (foreign key)
1   Olivia    1
2   Maria     1
1   Olivia    2

those two tables show a one-to-many relationship:
- Maria's parent is bob
- Olivia's Parents are bob and tony

we can define a relation in Django's models:

```python

class Post(models.Model):
    title = models.TextField()
    body = models.TextField()


class Comment(models.Model):
    title = models.TextField()
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

Post --> comment

Post Tabel

id (primary Key) title
1                 first post
2                 second post

we have unique entries in name columns

Comment tabel

id  title          post_id (foreign key)
1   first comment    2
2   second comment   2
```

- ListView:  gives collection of entities: e.g. Post.objects.all() 
- DetailView: gives details of a particular entity: Post.objects.get(pk=pk)

- for a DetailView we need a special URL:
    - parametrized URL

    ```python
    path('post/<int:pk>', BlogDetailView, name='detail_post')
    ```
```html
<a href="/post/1">Post 1</a>

or

<a href="{% url detail_post 1%}">Post 1</a>
```

```html
<a href="/post/25">Post 25</a>

or

<a href="{% url detail_post 25%}">Post 25</a>
```

### Admin

Register model in your admin:

```python
# blog/admin.py

from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

### Static Files

We need to add some CSS to our project to improve the styling.

 **Default Static File Location**:

 - Django automatically looks for a folder named `static` within each app.
 - For example, for a **blog** app, the directory would be `blog/static/`.
 - This is similar to how Django handles template files (e.g., blog/templates/).

 - **Centralized Static Files**:
 **project-level static directory**: 
 - This requires setting up the `STATICFILES_DIRS`
  setting in **settings.py** to point to the centralized directory.

  ```python
  STATICFILES_DIRS = [BASE_DIR / 'my_static']

  ```

  - **`STATIC_URL`**:
  - The `STATIC_URL` setting defines the **URL location** where static files can be accessed in your project.
  - By default, this is often set to `/static/`

  - **`STATICFILES_DIRS`**:
  - It allows the inclusion of a centralized, **project-level static folder**.

We need to add the static files to our templates by adding {% load static %} to the top of base.html.

Because our other templates inherit from base.htm1, we only have to add this once. 

refactored base.html:

```html
<!-- templates/base.html -->
<html>
<head>
<title>Django blog</title>
{% load static %}  
<link rel="stylesheet" href="{% static 'css/base.css' %}">
</head>
```
```html
<!-- templates/base.html -->
{% load static %}
<html>
<head>
<title>Django blog</title>
<link href="{% static 'app_styles.css' %}" rel="stylesheet">
</head>

```

#### Rewrite DetailView to function based view

How does the function based version of detail view looks like?

```python
from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_detail_view(request, pk):
    #post = get_object_or_404(Post, pk=pk)
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("Post not found")
    return render(request, "post_detail.html", {"object": post})

```

#### Rewrite DetailView to TemplateView

```python
from django.views.generic import TemplateView
from django.http import Http404
from .models import Post  # Updated to use Post instead of Article

class PostDetailTemplateView(TemplateView):
    template_name = 'post_detail.html'  # Updated template name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = kwargs.get('pk')  # Retrieve the primary key from the URL
        
        # Query the database for the post
        try:
            context['post'] = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            raise Http404(f"Post not found for pk {post_id}")  # Raise a 404 error if the post doesn't exist
        
        return context
```

#### Improving the DetailView Page's Code

To make our life easier, we should update the link on the homepage so we can directly access individual blog posts from there. Swap out the current empty
link,<a href=""> for<a href="{% url 'post_detail' post.pk %}">.

But it is more common to use and add the `get_absolute_url` method to the Post model:


```python
from django.db import models
from django.urls import reverse

class Post(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"pk": self.pk}) 
```

- get_absolute_url is a widely used naming convention in Django to define the canonical URL for a model instance.
- The method is typically implemented in the model to return the URL where the specific instance can be accessed, like a detail view.
- It helps keep URLs DRY (Don’t Repeat Yourself) by centralizing their logic within the model.
- The `get_absolute_url` method is not required by Django, but some features and third-party packages may expect it to exist.
- For example, Django’s admin site will use it to add "View on Site" links for objects if get_absolute_url is defined in the model.
- Similarly, other tools or libraries may rely on it for object URL resolution.

see: https://docs.djangoproject.com/en/5.1/ref/models/instances/#get-absolute-url


### get_absolute_url() in 'detail_post.html'

we can take the simpler step of using 
<a href="{{ post.get_absolute_url }}">{{ post.title }}</a></h2>in the template instead.

```html
{% extends "base.html" %}

{% block content %}

    {% for post in post_list %}
        <div class="post-entry">
            <h2><a href="{{ post.get_absolute_url }}">{{ post.title }}</a></h2>
            <p>{{ post.body }}</p>
        </div>
    {% endfor %}


{% endblock content %}
```

### Tests

- Our Blog project includes new, untested functionality.
- The `Post` model now contains multiple fields.
- A user feature has been introduced for the first time.
- The project includes:
  - A **list view** displaying all blog posts.
  - A **detailed view** for each individual blog post.








