# Frameworks - Views & Templates

> Learning Goals
>- Understand how to test in Django
>- Request & Response objects and its methods
>- understanding the context object
>- Template language: Filters and Tags

**Last Session**

- we learned to create templates (html files in django)
    - we can store it either in our apps directory or
    - in a main project template folder (we have to tell django the path)
- we setup
    - views.py: class based views (more concise): we used TemplateViews & function based views
    - urls.py
    - template
- architectural pattern of most backend frameworks: MVC:
    - Model: define of database and its tables & define core business logic 
    - View: presenting the data
    - Controller:application logic
- architectural pattern used django MVT(U):
    - Model: define of database and its tables & define core business logic 
    - View: describe which data passed to our templates; application logic
    - Template: presenting the data
    - Url: UrlConfig: path('', my_view, name='home')
- HTTP request/response cycle:
    - client makes a request to the server
    - server sends responds to the client (browser) and sent data/html is rendered


## Test

- catching errors
- It’s important to add automated tests and run them whenever a codebase changes
- Tests require a small amount of upfront time to write but more than pay off later on.
- In the words of Django co-creator Jacob Kaplan-Moss, “Code without tests is broken as designed.”


- The Python standard library contains a built-in testing framework called unittest that uses **TestCase** instances
    - and a long list of assert methods to check for and report failures. 

Django’s testing framework provides several extensions on top of Python’s unittest.

1. these include a test client for making dummy Web browser requests,
2. several Django-specific additional assertions
3. some test case classes:

1. SimpleTestCase,
2. TestCase,
3. TransactionTestCase

- Generally speaking, **SimpleTestCase** is used when a database is unnecessary 
- while **TestCase** is used when you want to test the database.
- **TransactionTestCase** is helpful to directly test database transactions

- If you look within our **pages** app, Django already provided a **tests.py** file we can use. 
- Since no database is involved in our project, 
    - we will import **SimpleTestCase** at the top of the file. 

For our first tests, we’ll check 
- that the two URLs for our website (the homepage and about page) 
    - both return HTTP status codes of 200
- (status code 200  is the standard response for a successful HTTP request)

```python
# pages/tests.py
from django.test import SimpleTestCase

# Create your tests here.
class HomePageTests(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class AboutPageTest(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
```
To run the test write:

```bash
python manage.py test -v2
```

At the moment we are testing the actual URL route for
each page: `/` for the homepage and `/about` for the about page.

But remember that we also added a URL target name for each page in the pages/urls.py file. 

To do that we can use the very handy Django utility function **reverse**. 

Instead of going to a URL path first, it looks for the URL target name.

In general, it is a bad idea to hardcode URLs, especially in templates.

By using **reverse** we can avoid this.

For now, we want to test the URL names for our two  pages. 
Import **reverse** at the top of the file add then add a new unit test for each below.

```python
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomePageTests(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('my_home')) # my_home ; TEACHER: What caused this error?
        self.assertEqual(response.status_code, 200)

class AboutPageTest(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
```

Django provides us with another test method: **self.assertTemplateUsed**

Let’s make sure that the correct templates (home.html and about.html) are used on each page 

```python
from django.test import SimpleTestCase
from django.urls import reverse 

# Create your tests here.

class HomePageTests(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

class AboutPageTest(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about.html')
```

Django provides us with another test method: **self.assertContains**

to make sure that our responses display the expected content of
"<h1>Home</h1>" and "<h1>About</h1>" 

respectively.

We can use *assertContains* to achieve this.

```python
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class HomePageTests(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_template_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<h1>Homepage</h1>')
        # self.assertIn(b'<h1>Homepage</h1>', response.content)


class AboutPageTest(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about.html')

    def test_template_content(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, '<h1>About page</h1>')

```

## Request and Response Objects in Django

Django views handle HTTP requests and return HTTP responses. 

- The `request` object provides information about the client's request, 
- while the `response` object defines what is sent back.

### Request Object

- All views receive a `request` object as the first argument.
- It contains attributes and methods for accessing request details:
1. **`request.method`**: The HTTP method used (`GET`, `POST`, etc.).
2. **`request.GET`**: Query parameters in the URL (`?key=value`).
3. **`request.POST`**: Data from an HTML form submitted via POST.
4. **`request.COOKIES`**:Dictionary of cookies sent by the client.
5. **`request.FILES`**: Uploaded files in the request.
6. **`request.META`**: Server metadata, including headers.
    - Provides a dictionary of all the metadata related to the request, such as HTTP headers, server details, and more.
    - Common headers in `request.META` include:
        - `'HTTP_USER_AGENT'`:The user agent string of the client.
        - `'HTTP_HOST'`: The host name.
        - `'REMOTE_ADDR'`: The client's IP address.

- Views must return a response object.
- Django provides several response classes:
1. **`HttpResponse`**: Basic response object for sending text or HTML.
2. **`render`**: Combines a template and context to create an `HttpResponse`.
3. **`JsonResponse`**: Sends JSON data.
4. **`HttpResponseForbidden`**:
5. **`HttpResponseServerError`**:

#### Methods and Attributes
- `.write(content)`: Appends content to the response body. 
    - (Similar to file objects)
- `.set_cookie(key, value)`: Sets a cookie in the response.
- `.delete_cookie(key)`: Deletes a cookie.

```python
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden, HttpResponseServerError 
from django.shortcuts import render
from django.views.generic import TemplateView

def home_page_view(request):
    # print("Request Object:", request)
    # print("Method: ", request.method )
    # print("Query Parameters: ", request.GET)
    # print("Cookies: ", request.COOKIES)
    # user_agent = request.META.get('HTTP_USER_AGENT')
    # print("User Agent: ", user_agent)
    # client_ip = request.META.get('REMOTE_ADDR')
    # print("Client IP:", client_ip)
    print('HTTP Response: ', HttpResponse('Bla'))
    #return HttpResponse('Hello World')
    print('HTTP JSON: ', JsonResponse({'status': 'success', 'message': 'Hello'}))
    #return JsonResponse({'status': 'success', 'message': 'Hello'})
    print('HTTP Forbidden: ', HttpResponseForbidden('Not allowed'))
    #return HttpResponseForbidden('Not allowed')
    print('HTTP ServerError: ', HttpResponseServerError('Error'))
    return HttpResponseServerError('Error')
    print('HTTP JSON: ')
    my_render = render(request, "home.html")
    print('render: ', my_render)
    return render(request, "home.html")
    

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"
```

- **Testing Response Content**:
    - `response.status_code`: HTTP status code (e.g., `200`, `404`).
    - `response.content`: Full response content in bytes.
    - `response.cookies`: Cookies set in the response.

### The Django Template Language: Using Variables in Templates

#### **Step 1: Pass Variables from the View**

- Variables must be passed to templates via a context dictionary in the view.


- **Example View:**
  ```python
  from django.shortcuts import render
  from datetime import datetime

  def home_page_view(request):
      context = {
          'title': 'Welcome to My Site',  # String data
          'today': datetime.now(),       # DateTime object
          'numbers': [1, 2, 3],          # List of numbers
          "dic": {"one": 1, "two": 2}
      }
      return render(request, 'home.html', context)
  ```

#### **Step 2: Access Variables in the Template**
- Variables from the context are accessed in the template using `{{ variable_name }}`.
- The code in {{ }} is a special templating language used to embed content in the template.
- The dot (.) can be used to access elements in lists and dictionaries.

- **Example Template:**
  ```html
  {% extends "base.html" %}

  {% block content %}
  <body>
      <h1>{{ title }}</h1>  <!-- Renders: Welcome to My Site -->
      <p>Today's date: {{ today }}</p>  <!-- Renders today's date -->
      <p>Numbers: {{ numbers }}</p>  <!-- Renders: [1, 2, 3] -->
      <h2>{{ items.0 }}</h2>
      <h3>{{ dic.one }}</h3>
  </body>
  {% endblock content %}
  ```