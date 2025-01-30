# Django - Users - 01: Authentication

# User Accounts

So far, we've built a working Blog application with forms but still need a major piece of most web applications: 

**user authentication**.

Implementing proper user authentication is famously hard;

Fortunately, Django has a powerful, 
built-in user authentication system that we can use and customize as needed.

Whenever you create a new project, by default, Django installs the **auth app**, which provides us with a User object containing:

- username
- password
- email
- first_name
- last_name

We will use this User object to implement login, logout, and signup in our blog application.

### Log In

Django provides us with a default view for a login page via LoginView. 

All we need to add are 

- a URL pattern for the auth system,
- a login template, and 
- a minor update to our django_project/settings.py file.

First, update the django_project/urls.py file. 

We'll place our login and logout pages at the accounts/ URL:

```python
# django_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")), # new
    path("", include("blog.urls")),
]
```

As the LoginView documentation notes 
(https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.views.LoginView),

by default Django will look within a templates directory called registration for a file called login.html for a login form.

-------------------
**Side NOTE**
you can specifiy the template_name:

```python
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Custom template for login
    path('login/', auth_views.LoginView.as_view(template_name='your_custom_folder/custom_login.html'), name='login'),
]

```
-------------------------

So we need to create a new directory called registration and the requisite file within it. From the command line, type Control+c to quit
our local server. Then create the new directory.

```Shell
(.venv) $ mkdir templates/registration
```

And then, with your text editor, create a new template file, templates/registration/login.html, filled with the following code:

```html
<!-- templates/registration/login.html -->
{% extends "base.html" %}
{% block content %}

<h2>Log In</h2>
<form method="post">{% csrf_token %}

{{ form.as_p }}

<button type="submit">Log In</button>
</form>
{% endblock content %}
```

We're using HTML <form></form> tags and specifying the POST method since we're sending data to the server (we’d use GET if we were requesting data, such as in a search engine form). 

We add {% csrf_token %} for security concerns to prevent a CSRF Attack. The form’s contents are outputted between
paragraph tags thanks to {{ form.as_p }} and then we add a “submit” button.

The final step is to specify where to redirect the user upon successful login.
 We can set this with the LOGIN_REDIRECT_URL setting. 

 At the bottom of the django_project/settings.py file, add the following:

 ```python
# django_project/settings.py
LOGIN_REDIRECT_URL = "home" # new
```

Now the user will be redirected to the 'home ' template, which is our homepage.

Upon entering the login info for our superuser account, we are redirected to the homepage.

Notice that we didn’t add any view logic or create a database model because the Django auth system provided both for us automatically. 

### Updated Homepage

Let’s update our base.html template so we display a message to users whether they are logged in or not. We can use the is_authenticated attribute for this.

Update the base.html file with new code:

```html
<!-- templates/base.html -->
{% load static %}
<html>
<head> 
<title>Django blog</title>

<link href="{% static 'css/base.css' %}" rel="stylesheet" s> 
</head>
<body> 
<div> 
<header> 
<div class="nav-left"> 
<h1><a href="{% url 'home' %}">Django blog</a></h1>

</div>

<div class="nav-right">

<a href="{% url 'post_new' %}">+ New Blog Post</a>

</div>
</header>
<!-- start new HTML... -->

{% if user.is_authenticated %} 
<p>Hi {{ user.username }}!</p> 

{% else %}
<p>You are not logged in.</p>
<a href="{% url 'login' %}">Log In</a>
{% endif %}
<!-- end new HIML... -->
{% block content %}
{% endblock content %}
</div>
</body>
</html>
```

If the user is logged in, we say hello to them by name; if not, we provide a link to our newly created login page.