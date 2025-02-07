### Django REST Framework - 2: DetailView & Tests 

> Learning Goals
>- Testing API
>- DetailView in Django restful API
>- Consume an API with curl, Postman and requests

**Last Session**

- Difference between traditional Django project and an API Django project:
    - tradition django responses with web page (`html/text`)
        - this means we have css, js, images, videos
    - web APIs don't have static files and  return instead of `html/text` data in `json` format
    - data can be programmatically easier accessed
- restful Django is on top of a traditional django project installed:

1. `pip install djangorestframework`
2. add rest_framework to APPS


in traditonal Django we need: 

1. urls.py files
2. models.py
3. 1.  views.py
3. 2.  forms.py (optional)
4. Templates
5. staticfiles

in django web API we need:
1. urls.py
2. views.py
3. serializers.py
4. models.py / that's where our Data comes from

we can still use the admin page by registering our model in admin.py

- we used `python manage.py startapp apis` to place all api related django code in the `apis` app

### Tests

Testing in Django relies upon Python’s built-in unittest module and several helpful Django-specific extensions.
- Most notably, Django comes with a test `client`

(see https://docs.djangoproject.com/en/4.2/topics/testing/tools/#the-test-client)

that we can use to simulate GET or POST requests, check the chain of redirects in a web request, and check that a given Django template is being used and has
the proper template context data.

Django REST Framework provides several additional helper classes that extend Django’s existing test framework. 

One of these is API Client, an extension of Django’s default Client, which we will use to test retrieving API data from our database.

```python
# apis/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Django for APIs",
            subtitle="Building APIS",
            author="Vincent",
            isbn='1234',
        )

    def test_api_listview(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(Book.objects.all()), 1)
        self.assertEqual(Book.objects.count(), 1)
        #print(response.data)
        self.assertEqual(len(response.data), 1)
        self.assertContains(response, self.book)
```
We extend APITestCase in a new class called APITests that starts by configuring set up data.

Second we confirm that HTTP status code matches 200.
Third we check that there is a single entry in the database. 

And finally we confirm that the response contains the title from our created book object.

Then run the test:

`(.venv) > python manage.py test`


In larger websites with hundreds or even thousands of tests, performance can become an issue and sometimes you want to check just test within a given app before running the full website test suite.

To do that,
simply add the name of the app you wish to check to the end of python manage.py test.

`(.venv) > python manage.py test apis`


