### Django REST Framework

As we saw, adding Django REST Framework is just like installing any other third-party app.

`(.venv) > pip install djangorestframework`


We have to formally notify Django of the new installation in our django_project/settings.py file.
Go to the INSTALLED_APPS section and add rest_framework.

```python
# django_project/settings.py
INSTALLED_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes"”,
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",
# 3rd party
"rest_framework", # new
# Local
"books",

]
```

Our web API will expose a single endpoint that lists out all books
in JSON.

For now though, to keep the API logic clear from the
traditional Django logic, we will create a dedicated apis app for our project.
`(.venv) > python manage.py startapp apis`

and that in settings

```python
# django_project/settings.py
INSTALLED_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes"”,
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",
# 3rd party
"rest_framework", # new
# Local
"books",
'apis',
]
```


### URLs

Let’s start with our URL configs.

adding an API endpoint is just
like configuring a traditional Django URL route.

In the project-level django_project/urls.py file include the apis app and configure its
URL route, which will be at api/.

```python
# django_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include('apis.urls')), # new
    path("", include("books.urls")),
]
```

Then create a new file called apis/urls.py.

This file will import a future view called BookAPIView and set it to the URL route
of "" so it will appear at api/.

As always, we’ll add a name to it as well, book_list, which helps in the future when we want to refer to this specific route.

```python
# apis/urls.py
from django.urls import path
from .views import BookAPIView

urlpatterns = [
    path("", BookAPIView.as_view(), name="book_ list"),
]
```

### Views

Django REST Framework views rely on a model and a serializer

Update the apis/views.py:

```python
# apis/views.py
from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer

class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
```

The only two steps required in our view are to specify the queryset, which
is all available books,
and then the serializer_class which will be
BookSerializer.

### Serializers

A serializer translates complex data like querysets and model instances into
a format that is easy to consume over the internet, typically JSON.

It is also possible to “deserialize” data, literally the same process in reverse, whereby
JSON data is first validated and then transformed into a dictionary.

```python
# apis/serializers.py
from rest_framework import serializers
from books.models import Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:

        model = Book
        fields = ("title", "subtitle", "author", "isbn") # try out a list
```

### Browsable API

Raw JSON data is not particularly friendly to consume with human eyes.

Fortunately, Django REST Framework ships with a built-in browsable API
that displays both the content and HTTP verbs associated with a given endpoint.

Django REST Framework provides this visualization by 
default.


It displays the HTTP status code for the page, which is 200 meaning OK.

Specifies Content-Type is JSON.

And displays the information for our single book entry in a formatted manner.

If you click on the “Get” button in the upper right corner and select “json” at
the top of the dropdown list you'll see what the raw API endpoint looks like.

