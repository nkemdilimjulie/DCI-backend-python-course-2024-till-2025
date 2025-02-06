Django - allauth - 01: email

to setup email verification, we can use `allauth`:

1. install

```pip install django-allauth```

2. django_project/settings.py
```python
INSTALLED_APPS = [
    ...
    'django.contrib.sites',  # required for allauth
    'allauth',
    'allauth.account',
    ...
]

SITE_ID = 1
```

3. allauth email setup:

```python
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # default
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Set email verification as mandatory
ACCOUNT_EMAIL_REQUIRED = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
4. migrate
```python manage.py migrate```

5. also add `allauth` middleware:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'allauth.account.middleware.AccountMiddleware',
    # Register your custom middleware
    'blog.middleware.ProtectSpecificRoutesMiddleware',
]
```

django_project/urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")), # FIRST !!!! so that accounts/templates/account signup.html is loaded before the templates from allauth.urls
    path("accounts/", include("allauth.urls")),
    path("my_accounts/", include("django.contrib.auth.urls")), 
    path('', include('blog.urls')),
]
```

- accounts/templates/account/   # path for allauth

```html
{% extends "base.html" %}

{% block content %}
<h2>Hello World</h2>

<form method="POST" action="">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign Up</button>
</form>

{% endblock %}
```

blog/templates/base.html

```html
    <header>
    <div class="nav-left">
        <h1><a href="{% url 'home' %}">Django Blog</a></h1>
    </div>
    <div class="nav-right">
        <h1><a href="{% url 'post_new' %}">+ New Blog Post</a></h1>
    </div>
    {% if user.is_authenticated %}
        <p>Hi {{ user.username }}!</p>
        <p><a href="{% url 'logout' %}"> Log out</a></p>
    {% else %}
        <p>You are not logged in.</p>
        <a href="{% url 'account_login' %}">Log In</a>  <!--New-->
        <a href="{% url 'account_signup' %}">Sign Up</a>
    {% endif %}
    <a href="{% url 'toggle_theme' %}">Toggle Theme</a>
    </header>
```