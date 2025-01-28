# Django - Blog App - 03: Slug applied & Django Forms

> Learning Goal
>- Understanding and Implementing Slug to our parametrized routes (urls.py)
>- understanding of CreateView: here we can create a new entity for a specific tables (model)
>- understanding django Forms 
>- CreateView vs function based view & TemplateView
>- UpdateView & DeleteView

**Last Session**
when do we need STATIC_FILES_DIR and when not?
- is used when we want to have a project-level static folder
- we can omit STATIC_FILES_DIR when our static folder is located an app folder
- Remark: it is analog to Templates folder

Why should we use a DetailView?
- to get a single record (e.g. with id = 5) from a table/model

```python

#urls.py
.... path('post/<int:id>', BlogView.as_view(), name='post_detail')

class BlogView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        post_id = kwargs.get('id') # integer of the row where are interested in
        post = self.model.objects.get(id=post_id) # instance of my model/ A row of my table with all its fields e.g. post.title, post.body .....
        return {'post': post}
```

models.py:

```python
class Post...
......
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'id': self.id})

```

Why did we implemented the method `get_absolute_url()` in the Post model?
- returns the path of our domain for a specific post: in the template we used

in my `post_list.html`:
<ul>
{% for post in post_list %}  # post_list: QuerySet[Post object 1, post object 2, etc]
    <li>
        <a href="{{ post.get_absolute_url }}">{{ post.title }}</a>  
    </li>
{% endfor %}
</ul>


---->

```html
<ul>
    <li>
        <a href="/post/1">M first Post</a>  
    </li>
    <li>
        <a href="/post/2">M 2nd Post</a>  
    </li>
</ul>

```

- using get_absolute_url in your models is a strong convention and might be used by 3-party lib for Django

### Replacing int:id slug:slug 

1. update model
2. update blog/urls

```python
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)  # If a user is deleted, their posts are deleted too
    body = models.TextField()

    def __str__(self):
        return self.title

```

- this will get us a 
    `django.db.utils.IntegrityError: UNIQUE constraint failed: new__blog_post.slug`
Why?
- First we have to create the fields without unique constraint
- then we have to create a method to save unique values to the slug column for existing rows
- we will overwrite the save method to do that
- remove unique constraint

```python
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(default='my_slug', max_length=200, blank=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)  # If a user is deleted, their posts are deleted too
    body = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        base_slug = f"{slugify(self.title)}"
        self.slug = base_slug
        return super().save(*args, **kwargs)

```

to overwrites all existing rows:
open the django shell: `python manage.py shell`
- then write:

```python
from posts.models import Post
posts = Post.objects.all()

for post in posts:
    post.save()
```

- Now that all rows are unique add unique constrain:

```python
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)  # If a user is deleted, their posts are deleted too
    body = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        base_slug = f"{slugify(self.title)}"
        self.slug = f"{slugify(self.title)}"
        return super().save(*args, **kwargs)

```

- next, adjust `get_url_absolute`:

```python
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)  # If a user is deleted, their posts are deleted too
    body = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        base_slug = f"{slugify(self.title)}"
        self.slug = f"{slugify(self.title)}"
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Generate URL using the slug instead of pk
        return reverse('post_detail', kwargs={"slug": self.slug})
```

and finally we have to adjust the urls.py

```python
from django.urls import path
from .views import BlogListView, BlogDetailTemplateView, BlogDetailView, blog_detail_view

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    # path("post/<int:pk>/", BlogDetailTemplateView.as_view(), name="post_detail"),
    path("post/<slug:slug>/", BlogDetailView.as_view(), name="post_detail"),

]
```

# Forms

HTML forms are one of the more complicated and error-prone aspects of web development because any time you accept user input, there are security concerns. 

All forms must be properly rendered, validated, and saved to the database.

Writing this code by hand would be time-consuming and difficult, so Django comes with powerful built-in Forms that abstract away much of the difficulty
for us. 

Django also comes with generic editing views for common tasks like displaying, creating, updating, or deleting a form.

### CreateView

### CreateView

To start, update our base template to display a link to a page for entering new blog posts.

It will take the form <a href="{% url 'post_new' %}"></a> where post_new is the name for our URL.

Your updated file should look as follows: 


```html
<!-- templates/base.html -->
{% load static %}
<html>
    ........
<body>
    <div>
        <header>
            <!-- start new HTML... -->

            <div class="nav-left">
                <h1><a href="{% url 'home' %}">Django blog</a></h1>
            </div>

            <div class="nav-right">
                <a href="{% url 'post_new' %}">+ New Blog Post</a>
            </div>

            <!-- end new HTML... -->
        </header>

        {% block content %}

        {% endblock content %}
    </div>
</body>
</html>
```

- add a new URL for post_new 
- Import BlogCreateView
- add a URL path for post/new/
- give it the URL name post_new to refer to it later in our templates

``python
# blog/urls.py
from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView # new

urlpatterns = [
    path("post/new/", BlogCreateView.as_view(), name="post_new"), # new
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("", BlogListView.as_view(), name="home"),
]
```

- create our view by importing a generic class-based view called CreateView at the top and then subclass it to create a new view called BlogCreateView.

```python
# blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView # new
from .models import Post
class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class BlogCreateView(CreateView): # new
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]

```

Within BlogCreateView, we specify our database model, Post, the name of our template, post_new.html, and explicitly set the database fields we want to expose, which are title, author, and body.

The last step is creating our template, templates/post_new.html:

```html
<!-- templates/post_new.html -->
{% extends "base.html" %}
{% block content %}
    <h1>New post</h1>
    <form action="" method="post">{% csrf_token %}
    {{ form.as_p }}
        <input type="submit" value="Save">
    </form>
{% endblock content %}
```

Let’s break down what we've done:

- on the top line we extended our base template.
- use HTML <form> tags with the POST method since we’re sending data.
- If we were receiving data from a form, for example, in a search box, we would
use GET.
- add a {% csrf_token %} which Django provides to protect our form from cross-site request forgery.
You should use it for all your Django forms.
- then, to output our form data use {{ form.as_p }}, which renders the specified fields within paragraph <p> tags.
- finally, specify an input type of submit and assign the value “Save”.


### Function-Based View for Blog Creation

To rewrite the `BlogCreateView` class-based view (`CreateView`) into a function-based view, 
- you can use Django's `ModelForm` and handle the form submission manually in the view.


### **Function-Based View for Blog Creation**

```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import ModelForm
from .models import Post

# Define the ModelForm for the Post model
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "author", "body"]

# Function-based view for creating a new post
def blog_create_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to create a new Post
            return redirect("home")  # Redirect to the post list view (or any desired page)
    else:
        form = PostForm()

    return render(request, "post_new.html", {"form": form})
```


If you want to mimic a `CreateView` using `TemplateView`, you need to handle form rendering, validation, and saving manually inside the `TemplateView`.

### **Implementation of a Create-like View with TemplateView**

```python
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.forms import ModelForm
from .models import Post

# Define a ModelForm for the Post model
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "author", "body"]

# Mimicking CreateView with TemplateView
class BlogCreateView(TemplateView):
    template_name = "post_new.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PostForm()  # Add an empty form to the context
        return context

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new post
            return redirect("post_list")  # Redirect to the post list (or another page)
        return self.render_to_response({"form": form})  # Re-render the template with the form and errors
```

1. `get_context_data`:
   - Prepares the form for rendering when the user accesses the page via a `GET` request.
   - Adds the empty `PostForm` instance to the context.

2. `post`:
   - Handles `POST` requests when the form is submitted.
   - Validates the form, saves the post if valid, and redirects to the desired page.
   - If the form is invalid, re-renders the template with the form and its errors.