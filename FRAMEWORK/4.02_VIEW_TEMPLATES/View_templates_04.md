# Django - Views & Templates - 04: Mixins

> Learning Goal
>- Applying Mixins
>- Intro Model & ORM
>- Admin

**Last Session**

- tags: e.g. {% load %} , {% if number ==2 %} {% endif %}; {% for item in items %} {% endfor %}
- filter: e.g. {{ 'HELLO'|lower }}, {{ number|'2' }}, {{ today|date: 'd M Y'}}
- we can create custom tags (and custom filters)

- HTTP Methods: GET, POST, PUT, PATCH, DELETE

- generic class-based View Lifecycle: TemplateView -> dispatch -> get()(-->get_context_data())/post()/put()/patch()/delete()/http_method_not_allowed()

```python
def home_func_view(request):
    context = {
        'key1': 'value1',
        'key2': 'value2',
        'title': 'Hello World',
    }
    return render(request, "home.html", context)

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = {
            'key1': 'value1',
            'key2': 'value2',
            'title': 'Hello World',
        }
        return context

```


## Using a Mixin in a Django View

Mixins are a way to reuse code across multiple class-based views.
They can be particularly useful when certain patterns of behavior are needed across multiple views.

### 1. Defining the Mixin

First, let's define a mixin that checks if the user's browser accessing the view has a cookie with a special value stored. 


Create `mixin class` :

```python
from django.http import HttpResponseForbidden

class ActiveUserRequiredMixin(object):
    """
    Mixin to ensure the user is active.
    """
    #class ActiveRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.COOKIES.get('my_cookie') == 'my_cookie_value':
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseForbidden('You are not allowed to access')
```

### 2. Applying the Mixin to a View

Now that we have our mixin ready, let's apply it to a view. For this example, we'll use a basic `TemplateView`.

```python
from django.views.generic import TemplateView

class DashboardView(ActiveUserRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
```

- the mixin should come before the view base class. 
- This is because the `dispatch` method in the mixin should be the first one to be invoked.

### 3. Configuring the URL

Ensure that the view is reachable by configuring its URL in your `urls.py`.

```python
from django.urls import path
from .views import DashboardView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
```

### 4. Testing the Mixin

1. Run your Django server.
2. Navigate to the `/dashboard/` URL.
3. If there is a cookie with a value my_cookie_value' you would access the dashboard page
4. other you would be directed to `HttpResponseForbidden('You are not allowed to access')`


Add Extra Context Dynamically with the help of Mixins:

- Understand how to use a mixin to inject additional context variables into your templates without modifying the core view logic.

#### Steps:

1. **Set Up the Django Project:**

   - Create a new Django app within the project:
     ```bash
     python manage.py startapp myapp
     ```

   - Add `myapp` to the `INSTALLED_APPS` list in `django_projects/settings.py`.

2. **Create the Mixin:**

   - In `myapp/mixins.py`, create the `ExtraContextMixin` mixin:
     ```python
     class ExtraContextMixin:
         extra_context = None

         def get_context_data(self, **kwargs):
             context = super().get_context_data(**kwargs)
             if self.extra_context:
                 context.update(self.extra_context)
             return context
     ```

3. **Create the View:**

   - In `myapp/views.py`, create a view using the `ExtraContextMixin`:
```python
from django.views.generic import TemplateView
from .mixins import ExtraContextMixin

class MyView(ExtraContextMixin, TemplateView):
    template_name = 'my_template.html'
    extra_context = {'key': 'value'}
```

4. **Set Up the Template:**

   - In the `myapp/templates/` directory, create a template called `my_template.html`:
     ```html
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <title>My Template</title>
     </head>
     <body>
         <h1>Welcome to My Template</h1>
         <p>Key value from extra context: {{ key }}</p>
     </body>
     </html>
     ```

5. **Configure the URL:**

   - In `myapp/urls.py`, add the URL pattern for the view:
     ```python
     from django.urls import path
     from .views import MyView

     urlpatterns = [
         path('', MyView.as_view(), name='my_view'),
     ]
     ```

   - Include `myapp`'s URLs in the main `urls.py` of the project:
     ```python
     from django.contrib import admin
     from django.urls import path, include

     urlpatterns = [
         path('admin/', admin.site.urls),
         path('', include('myapp.urls')),
     ]
     ```

6. **Run the Server and Test:**

   - Run the development server:
     ```bash
     python manage.py runserver
     ```

   - Open your browser and navigate to `http://127.0.0.1:8000/`. You should see the message "Key value from extra context: value" displayed on the page.