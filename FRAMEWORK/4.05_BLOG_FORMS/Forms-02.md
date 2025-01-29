# Django - Blog App - 02: UpdateView & DeleteView

> Learning Goals
>- DeleteView, UpdateView
>- reverse() vs reverse_lazy()


**Last Session**

- replacing integer parameters with Slug parameters in the urls.py
- we had to add column (SlugField) to an existing table that contain rows
- ```slug = models.SlugField(unique=True, max_length=200, blank=True)```
Why prevented the unique constrain to add that column?
- The problem was that for all existing rows a newly added column with have either null values or the same 
default values
- and this led to a  `UNIQUE constraint failed` error
How can we fix this?
1. Remove unique constraint in ```slug = models.SlugField(unique=True, max_length=200, blank=True)```
2. and instead we had a default value```slug = models.SlugField(default='my_slug', max_length=200, blank=True)```
2. 1. (```slug = models.SlugField(null=True, max_length=200, blank=True)``` would had also worked) 
3. 1. we had to fill the values of the Slug column with unique values
3. 2. for that we use a built-in function slugify; that function we used to slugify the title
3. 3. in order that also future rows contain unique slug values we had to overwrite the `save()` method

```python
class Post(models.Model):
    titel = models.CharField(.....)
    slug = models.SlugField(default='my_slug', max_length=200, blank=True)
    .....

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

```

3. 4. we looped over all rows and called our newly overwritten save method

```python
# in python manage.py shell

from blog.models import post

for post in Post.objects.all():
    post.save()
```

after that we were able to add the unique constraint to our slug column:

```python
class Post(models.Model):
    titel = models.CharField(.....)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    .....

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

```

- CreateView
    - When would you use a CreateView?
        - when we want to create a new instance of our models
        / When we want that our users of our web site can create new entries in our database tables
    - What type of requests are supported by the CreateView?
        - GET & POST
        - and therefore we have `get()` and `post()` methods
        
```python
class BlogCreateView(CreateView):
    model = Post
    template_name = "post_detail.html"
    fields = ["title", "author", "body"] # tells django which fields from our model should be included in this form
```

### UpdateView

- use forms like the CreateView so that user can update their data related to our website

- add a new link to the post_detail.html so that the option to edit a blog post appears on an individual blog page

```html
<!-- templates/post_detail.html -->

{% extends "base.html" %}

{% block content %}

<div class="post-entry">

<h2>{{ post.title }}</h2>
<p>{{ post.body }}</p>

</div>

<!-- start new HTML... -->

<a href="{% url 'post_edit' post.pk %}">+ Edit Blog Post</a>

<!-- end new HTML... -->

{% endblock content %}
```

We've added a link using <a href>...</a>and the Django template engine’s {% url ... %} tag. Within it, we've specified the target name of our 'URL, which will be called post_edit, and also passed the parameter needed, which is the primary key of the post: post.pk.

```html
<!-- templates/post_edit.html -->

{% extends "base.html" %}

{% block content %}

<h1>Edit post</h1>
<form action="" method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Update">
</form> 
{% endblock content %}
```

 We again use HTML <form></form> tags
- Django’s csrf_token for security
- form.as_p to display our form fields with paragraph tags
- the input tag gives us the the submit button.

Next comes the view.
here we have to subclass our new view BlogUpdateView with UpdateView 

```python
# blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView # new
from .models import Post
class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html" 

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView): # new
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]
```

Notice in BlogUpdateView we assume that the author of the post is not changing;
we only want the title and body text to be editable, hence ["title", "body" ] but not author as is the case for BlogCreateView.

The final step is to update our urls.py file as follows:

```python
# blog/urls.py
from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView, # new
)

urlpatterns = [
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"), # new
    path("", BlogListView.as_view(), name="home"),
] 
```
- create a new URL pattern for /post/pk/edit and give it the name post_edit

#### function based Version

```python
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ["title", "body"]


def post_update_view(request, pk):
    post =get_object_or_404(Post, pk=pk) # Post.objects.get(pk=pk)

    if request.method == "POST":
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            # print('POST: ',post)
            # print('POST REQUEST: ', request.POST)
            return redirect('post_detail', slug=post.slug)
    elif request.method == "GET":
        form = PostUpdateForm(instance=post)

    return render(request, 'post_edit.html', {'form': form })
```

1. **`get_object_or_404()`**:
   - Fetches the `Post` object by `pk`. Returns a 404 error if it doesn't exist.

2. **`PostForm`**:
   - A form class for the `Post` model. Make sure to create this form if it doesn't already exist.

3. **Redirection**:
   - After successfully updating, the user is redirected to the detail page using `HttpResponseRedirect`.


### DeleteView

adding a link to delete blog posts on our individual blog page, post_detail.html.

```html 
<!-- templates/post_detail.html -->
{% extends "base.html" %}
{% block content %}
<div class="post-entry">
    <h2>{{ post.title }}</h2>
    <p>{{ post.body }}</p>
</div>
<div>
<!-- start new HTML... -->
    <p><a href="{% url 'post_edit' post.pk %}">+ Edit Blog Post</a></p>
    <p><a href="{% url 'post_delete' post.pk %}">+ Delete Blog Post</a></p>
<!-- end new HTML... -->
</div>
{% endblock content %}
```

Then create a new file for our delete page template. It will be called templates/post_delete.html and contain the following code:


```html
<!-- templates/post_delete.html -->
{% extends "base.html" %}
{% block content %}
<h1>Delete post</h1>
<form action="" method="post">{% csrf_token %}
    <p>Are you sure you want to delete "{{ post.title }}"?</p>
    <input type="submit" value="Confirm">
</form>
{% endblock content %}
```

Now update the blog/views.py file by importing DeleteView and reverse_lazy at the top and then create a new view that subclasses DeleteView.

```python
# blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # new
from django.urls import reverse_lazy # new
from .models import Post

    .....
    .....
    .....
    .....

class BlogDeleteView(DeleteView): # new
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
```


- The DeleteView specifies a model which is Post
- a template which is post_delete.html
- a third field called `success_url`

after a blog post is deleted, we want to redirect the user to another page which is, in our case, the homepage at `home`.

we are using `reverse_lazy` here and not reverse. 
Both reverse and `reverse_lazy `perform the same
task: generating a URL based on an input like the URL name. 

The difference is when they are evaluated.
reverse executes right away,
so when BlogDeleteView is executed, immediately the model, template_name,and success_url methods are loaded. 

But the `success_url` needs to find out what the resulting URL path is associated with the URL name “home.” 

reverse() in a class based view can’t always do that in time.  # revers('home') --> /my_home
That’s why we use `reverse_lazy` in this example

it delays the actual call to the URLConf until the moment it is needed, not when our class BlogDeleteView is being evaluated.
The moment BlogDeleteView is called, reverse needs to have the information from the URLconf about what the proper route is for the URL name “home.”

***https://docs.djangoproject.com/en/4.2/ref/urlresolvers/#reverse-lazy**

