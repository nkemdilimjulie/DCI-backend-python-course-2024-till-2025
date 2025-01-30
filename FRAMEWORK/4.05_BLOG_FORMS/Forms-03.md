# Django - Blog App - 03: Testing our CRUD Blog app & CSRF & Form widgets

> Learning Goals
>- understanding tests for create, update & delete operations
>- CSRF (disabling & simulate an csrf attack) 
>- adding Widgets to our Form class
>- authentication

**Last Session**

- UpdateView: modifies an existing row in a table
    - needs parameterized urls
    - as in the create view we had to add the `fields` class attribute
- DeleteView: removes an existing row in a table 
    - needs parameterized urls
    - we need to set the `success_url` class attribute
    What does the `success_url` class attribute do?
    This tells django where to redirect after successful deletion (e.g. of an post entry )

    ```python
    class BlogDeleteView(DeleteView):
        model = Post
        template_name = 'delete.html'
        success_url = reverse_lazy('home') # '/'
    ```
- Difference between reverse & reverse_lazy?
    - reverse_lazy returns the url when it is actual needed
        - it gives the urlConfig the necessary time to load
    - reverse is loaded immediately when the class is loaded
    - the class is loaded before urlConfig is completely loaded

- Why don't have my BlogCreateView and BlogUpdateView success_url attribute?
    - They check if we have the get_absolute_url method
        in our model and if yes get_absolute_url is used
        for redirect after a succesful POST request

**Quiz**

```python
e.g. for question 6
my_redirect_url = reverse('detail_post', args=[1])
```

## Tests

Time for tests to make sure everything works now - and in the future - as expected.

We've added new views for create, update, and delete, so that means three new tests:

- def test_post_createview
- def test_post_updateview
- def test_post_deleteview

Update your existing tests.py file with new tests

```python
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify
from .models import Post

class BlogTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user = User.objects.create_user(
            username="testuser",
            email="test@email.com",
            password='secret',
        )

        cls.post = Post.objects.create(
            title="A good title",
            body="Nice body content",
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, 'A good title')
        self.assertEqual(self.post.body, 'Nice body content')
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(str(self.post), 'A good title')
        self.assertEqual(self.post.get_absolute_url(), 
                                f"/post/{slugify(self.post.title)}/")

    def test_post_createview(self):
        response = self.client.post(
            reverse('post_new'),
            {
                'title': "New title",
                'body': 'New text',
                'author': self.user.id
            }

        )
        self.assertEqual(response.status_code, 302)
        # self.assertEqual(Post.objects.get(id=2).title, 
        #                     'New title')
        self.assertEqual(Post.objects.last().title, 
                            'New title')
        self.assertEqual(Post.objects.last().body, 
                            'New text')
        self.assertEqual(Post.objects.last().author,
                            self.user)
    def test_post_updateview(self):
        response = self.client.post(
            reverse("post_edit", args=[self.post.id]),
            {
                'title': 'updated title',
                'body': 'updated text'
            }
        ) 
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 
                            'updated title')
        self.assertEqual(Post.objects.last().body, 
                            'updated text')


    def test_post_deleteview(self):
        response = self.client.post(reverse('post_delete',
                                        args=['1']))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(bool(Post.objects.all()))   # empty collections/queryset are always falsy values and therefore bool(<QuerySet[]>) is False
```
- For `test_post_createview`, we create a new response and check that the page has a 302 redirect status code and that the last () object created on our model matches the new response.
- `test_post_updateview` sees if we can update the initial post created in setUpTestData
only data set in setUpTestData is available to all test methods
- `test_post_deleteview`, confirms that a 302 redirect occurs when deleting a post.


### Form class

Using Django's powerful ModelForm feature, the form is designed to handle both the rendering and data validation for creating or updating our models.

```bash
my_blog_app/
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py     <-- This is where forms.py goes
    ├── models.py
    ├── urls.py
    ├── views.py

```

```python
from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', "author", "body"]


class PostUpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', "body"]
        widgets = {
            'title': forms.TextInput(attrs={'class':
                        'my-input-class'}),
            'body': forms.Textarea(attrs={'class':
                        'my-input-class'}),
        }
```

- Inherits from `forms.ModelForm`
- `Meta` Inner Class: Provides configuration details about how the form should be constructed and behave
- `widgets`: Customizes the HTML rendering of the form fields:
      - The `title` field will render as an `<input type="text">` element with the CSS class "my-input-class".
      - The `content` field will appear as a `<textarea>` with the CSS class "my-textarea-class".

### CSRF Vulnerability

**Disclaimer:**
The content of this lesson is intended for educational purposes only. While we will be discussing Cross-Site Request Forgery (CSRF) attacks, including their mechanisms, potential impact, and countermeasures, the use of this knowledge should be strictly limited to ethical, responsible behavior and legal practices.
Please ensure you have appropriate permissions before attempting to test or apply any security techniques in live environments. Unauthorized use of security vulnerabilities, including but not limited to CSRF attacks, is illegal and unethical. Always follow best practices, legal guidelines, and ethical standards in your work as a developer or security professional.
The information shared in this session is not meant to encourage or endorse malicious behavior. It is vital to respect others' privacy, data, and systems at all times.

1. Disabling CSRF Protection in Django

To disable CSRF protection in Django:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection is disabled here
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
By commenting out the `'django.middleware.csrf.CsrfViewMiddleware'`, Django will not check for the CSRF token in requests, allowing the possibility for malicious cross-site requests.

- never do that in production !!!!

2. Simulating an attack

A **CSRF attack** occurs when an attacker tricks a user into making an unwanted request to a server where they are authenticated.

 Since the server trusts the user's credentials (e.g., session cookie), it will process the request, even though it was initiated by a malicious site.

 In this case, without CSRF protection, Django cannot differentiate between a legitimate form submission and a forged one.

3. Example: Malicious HTML Form

The attacker creates a malicious webpage with a form that sends a **POST request** to your server.
The form will simulate an action (like modifying data) without the user's consent, such as changing a post's title and body.

```html
<html>
<body>
    <h1>Attack Page</h1>
    <form action="http://127.0.0.1:8080/post/2/edit/" method="POST">
        <input type="hidden" name="title" value="Hacker1">
        <input type="hidden" name="body" value="You have been attacked again">
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

1. **The Attacker's Form**:
    - The form's `action` points to a URL on your server (`http://127.0.0.1:8080/post/2/edit/`) where an authenticated user might change the post data.
    - The form contains hidden fields (`title` and `body`) that the attacker controls.
        - When the user unknowingly submits this form, it will modify the post's title and body to values controlled by the attacker.
    
2. **No CSRF Token**:
    - Since we disabled CSRF protection by removing the middleware, 
    the form submission does not need a CSRF token.
    - If CSRF protection were enabled, Django would require a CSRF token, making this attack impossible unless the attacker has access to the CSRF token.

3. **Unknowingly Triggered by the User**:
    - If a user is logged in to your Django application and visits the malicious page (e.g., via a phishing link), the form will automatically submit when they click "Submit."
    - The server will accept this request because the session cookie is included automatically (since the user is logged in).

#### Conclusion
- we’ve built a blog application that allows for creating, reading, updating, and deleting blog posts. 
- This core functionality is known by the acronym CRUD: Create-Read-Update-Delete.
- The majority of websites in the world consist of this core functionality.

 however, a potential security concern:
    - currently any user can update or delete blog entries, not just the creator! 

Fortunately, Django has built-in features to restrict access based on permissions



