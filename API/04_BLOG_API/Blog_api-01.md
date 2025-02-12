# Django API - Blog - 1: CustomUser & combined CRUD

## Blog API

We will create a Blog API using the full set of Django REST Framework features.

It will have
1. users, 
2. permissions, and 
3. allow for full CRUD (Create-Read-Update-Delete) functionality. 

we will build the basic API section.
we start with traditional Django and then add in Django REST
Framework.

 we’ll be using a custom user mode

 ### Initial Set Up

 ```shell
 mkdir blog_api_live
 cd blog_api_live
 python3 -m venv .venv
 source .venv/bin/activate
 python3 -m pip install django
 django-admin startproject django_project .
 ```

 We are not running migrate yet
because we'll be using a custom user model and want to wait until it is configured before running our first migrate command.

### Custom User Model

first create a new app called accounts.

```shell
(.venv) > python manage.py startapp accounts
```

Then add it to our INSTALLED_APPS configuration so Django knows it exists.

```python
# django_project/settings.py
INSTALLED_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",
# Local
"accounts.apps.AccountsConfig", # new
]
```

Within accounts/models.py define a custom user model called CustomUser by extending AbstractUser

and adding a single field, name, for now.

We'll also a __str__ method to return the user’s email address in the admin and elsewhere.

```python
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)
```

- null is database-related. When a field has null=True, it can store a database entry as NULL, meaning no value.
- blank is validation-related.
If blank=True, then a form will allow an empty value, whereas if blank=False then a value is required.

In practice, null and blank are commonly used together in this fashion so that a form allows an empty value, and the database stores that value as NULL.

The last step is to update the AUTH USER MODEL configuration in settings.py, which is implicitly set to auth.User, over to accounts.CustomUser. 

This can be added at the bottom of the file.

```python
# django_project/settings.py
AUTH_USER_MODEL = "accounts.CustomUser" # new
```

Now we can run makemigrations for our model changes, migrate to initialize the database, and createsuperuser to create a superuser account so we can view the admin. 

```shell
(.venv) > python manage.py makemigrations
(.venv) > python manage.py migrate
(.venv) > python manage.py createsuperuser
```

Then launch Django’s internal web server with the runserver command:

```shell
(.venv) > python manage.py runserver
```
head on over to the admin at http://127.0.0.1:8000/admin/ and log in...
...something is missing...

Only the Groups section appears.
We don’t have Users as we normally would with the default User model.

What's missing is two things: 

1. we have to customize accounts/admin.py to display our new custom user model and 
2. create a new file called accounts/forms.py that sets CustomUser to be used when creating or changing users. 

#### Admin for Custom User

We'll start with accounts/forms.py.

```python
# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("name",) 

class CustomUserChangeForm(UserChangeForm): 
    class Meta: 
        model = CustomUser 
        fields = UserChangeForm.Meta.fields 
```

We’ll also import our CustomUser model so that it can be integrated into new CustomUserCreationForm and CustomUserChangeForm classes.

the last step in the custom user setup is to update accounts/admin.py to properly display the new custom user.

```python
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
    "email",
    "username", 
    "name",
    "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),) 
admin.site.register(CustomUser, CustomUserAdmin)
```

**class attribute in the `CustomUserAdmin` class:**
### 1. `add_form`
```python
add_form = CustomUserCreationForm
```
- **Purpose**: Specifies the form that will be used to create new users via the admin interface. 

### 2. `form`
```python
form = CustomUserChangeForm
```
- **Purpose**: Specifies the form used to edit or change user information in the admin interface.


### 3. `model`
```python
model = CustomUser
```
- **Purpose**: Defines the model that this admin class is related to.


### 4. `list_display`
```python
list_display = [
    "email",
    "username", 
    "name",
    "is_staff",
]
```
- **Purpose**: Defines the fields that will be displayed in the list view of the admin when viewing users.

### 5. `fieldsets`
```python
fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
```
- **Purpose**: Defines the layout of fields when viewing or editing a user.

**None in Fieldset**: This represents the title or label of the section in the admin form. Since it's None, no title will be displayed for this section.

### 6. `add_fieldsets`
```python
add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)
```
- **Purpose**: Specifies the layout of fields shown when adding a new user.


### `admin.site.register(CustomUser, CustomUserAdmin)`
- **Purpose**: Registers the `CustomUserAdmin` class with the `CustomUser` model in the Django admin site.


### Posts App

To create an app Posts run :

```shell
(.venv) > python manage.py startapp posts
```

Then immediately update INSTALLED_APPS in the django_project/settings.py file before we forget.

```python
# django_project/settings.py
INSTALLED_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",
# Local
"accounts.apps.AccountsConfig",
"posts.apps.PostsConfig", # new
]
```

### Post Model

Our blog Post database model will have five fields: author, title, body, created_at, and updated_at.

we will also import Django’s settings so we can refer to AUTH_USER_MODEL in our author field. 

And we'll add a __str__ method as a general best practice.

```python
# posts/models.py
from django.conf import settings
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

**auto_now_add=True**: This is an argument passed to the DateTimeField. It means that the date and time will be automatically set to the current date and time when a new record is created. Once set, it will not change, even if the record is updated later.

**auto_now=True**: This argument means that the date and time will be automatically set to the current date and time every time the record is saved, whether it's being created for the first time or being updated. This ensures that the field always reflects the last time the record was changed.

update our database by first creating a new migration file with the command makemigrations posts and then running migrate to sync the database with our model changes.


(.venv) > python manage.py makemigrations posts
(.venv) > python manage.py migrate

We want to view our data in Django’s admin app so we’ll quickly update posts/admin.py as follows.

```python
# posts/admin.py
from django.contrib import admin
from .models import Post
admin.site.register(Post)
```

### Tests

At the top of the file import get_user_model() to refer to our User along with TestCase and the Post model.

```python
# posts/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
        username="testuser",
        email="test@email.com",
        password="secret",
        )
        cls.post = Post.objects.create(
        author=cls.user,
        title="A good title",
        body="Nice body content",
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        
```

### Django REST Framework

As we have seen before, Django REST Framework takes care of the heavy lifting of transforming our database models into a RESTful API.

There are three main steps to this process:

- urls.py file for the URL routes
- serializers.py file to transform the data into JSON
- views. py file to apply logic to each API endpoint

On the command line use pip to install Django REST Framework.

```shell
(.venv) > python -m pip install djangorestframework
```

Then add it to the INSTALLED_APPS section of our django_project/settings.py file. 



```python
# django_project/settings.py
INSTALLED_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",
# 3rd-party apps
"rest_framework", # new
# Local
"accounts.apps.AccountsConfig",
"posts.apps.PostsConfig",
]
```


### URLs

```python
# django_project/urls.py
from django.contrib import admin
from django.urls import path, include # new
urlpatterns = [
path("admin/", admin.site.urls),
path("api/v1/", include("posts.urls")), # new
]
```

It is a good practice to always version your APIs since when you make a large change there may be some lag time before various consumers of the API can
also update.

That way you can support a v1 of an API for a period of time while also launching a new, updated v2 and avoid breaking other apps that rely on your API back-end.

Next create a new posts/urls.py file and add the following code:

```python
# posts/urls.py
from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [ 
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"), 
    path("", PostList.as_view(), name="post_list"), 
]
```
### Serializers

The serializer not only transforms data into JSON, it can also specify which fields to include or exclude. 

In our case, we will include the id field Django automatically adds to database models but we will exclude the updated_at field by not including it in our fields.

```python
# posts/serializers.py
from rest_framework import serializers
from .models import Post

    class PostSerializer(serializers.ModelSerializer):
        class Meta:
            fields = (
            "id",
            "author",
            "title",
            "body",
            "created_at",
            )
            model = Post
```

### Views

Django REST Framework has several generic views that are helpful.

We have already used ListAPIView in both the
Library and Todos APIs to create a read-only endpoint collection, essentially a list of all model instances.

In the Todos API we used RetrieveAPIView for a
read-only single endpoint, which is analogous to a detail view in traditional Django.

For our Blog API we want to list all available blog posts as a read-write endpoint which means using ListCreateAPIView, which is similar to the
ListAPIView we've used previously but allows for writes and therefore POST requests. 

We also want to make the individual blog posts available to be
read, updated, or deleted. 

for this purpose we used RetrieveUpdateDestroyAPIView.

```python
# posts/views.py
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

we create two views: 
1. PostList uses the generic **ListCreateAPIView** while 
2. PostDetail uses **theRetrieveUpdateDestroyAPIView**.

### Browsable API

(.venv) > python manage.py runserver

Then go to **http://127.0.0.1:8000/api/v1/** to see the Post List endpoint.

we have a model instance endpoint displaying a single post.

**http://127.0.0.1:8000/api/v1/1/**

You can see in the header that GET, PUT, PATCH, and DELETE are supported but not POST.


